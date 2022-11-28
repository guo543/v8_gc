#include "src/heap/snapshot-collector.h"

#include "src/objects/visitors.h"
#include "src/objects/objects.h"
#include "marking-worklist-inl.h"
#include "src/heap/objects-visiting.h"
#include "src/objects/objects-body-descriptors-inl.h"
#include "src/objects/objects-inl.h"

#include "src/heap/mark-compact.h"

#include <unordered_map>
#include <unordered_set>

#include "src/base/logging.h"
#include "src/base/optional.h"
#include "src/base/utils/random-number-generator.h"
#include "src/codegen/compilation-cache.h"
#include "src/common/globals.h"
#include "src/deoptimizer/deoptimizer.h"
#include "src/execution/execution.h"
#include "src/execution/frames-inl.h"
#include "src/execution/isolate-utils-inl.h"
#include "src/execution/isolate-utils.h"
#include "src/execution/vm-state-inl.h"
#include "src/handles/global-handles.h"
#include "src/heap/array-buffer-sweeper.h"
#include "src/heap/basic-memory-chunk.h"
#include "src/heap/code-object-registry.h"
#include "src/heap/concurrent-allocator.h"
#include "src/heap/evacuation-allocator-inl.h"
#include "src/heap/gc-tracer.h"
#include "src/heap/heap.h"
#include "src/heap/incremental-marking-inl.h"
#include "src/heap/index-generator.h"
#include "src/heap/invalidated-slots-inl.h"
#include "src/heap/large-spaces.h"
#include "src/heap/mark-compact-inl.h"
#include "src/heap/marking-barrier.h"
#include "src/heap/marking-visitor-inl.h"
#include "src/heap/marking-visitor.h"
#include "src/heap/memory-chunk-layout.h"
#include "src/heap/memory-measurement-inl.h"
#include "src/heap/memory-measurement.h"
#include "src/heap/object-stats.h"
#include "src/heap/objects-visiting-inl.h"
#include "src/heap/parallel-work-item.h"
#include "src/heap/read-only-heap.h"
#include "src/heap/read-only-spaces.h"
#include "src/heap/safepoint.h"
#include "src/heap/spaces-inl.h"
#include "src/heap/sweeper.h"
#include "src/heap/weak-object-worklists.h"
#include "src/ic/stub-cache.h"
#include "src/init/v8.h"
#include "src/logging/tracing-flags.h"
#include "src/objects/embedder-data-array-inl.h"
#include "src/objects/foreign.h"
#include "src/objects/hash-table-inl.h"
#include "src/objects/instance-type.h"
#include "src/objects/js-array-buffer-inl.h"
#include "src/objects/js-objects-inl.h"
#include "src/objects/maybe-object.h"
#include "src/objects/objects.h"
#include "src/objects/slots-inl.h"
#include "src/objects/smi.h"
#include "src/objects/transitions-inl.h"
#include "src/objects/visitors.h"
#include "src/snapshot/shared-heap-serializer.h"
#include "src/tasks/cancelable-task.h"
#include "src/tracing/tracing-category-observer.h"
#include "src/utils/utils-inl.h"

namespace v8 {
namespace internal {

class RootPrintVisitor : public RootVisitor {
 public:
  void VisitRootPointer(Root root, const char* description,
                        FullObjectSlot p) override {
    Object obj = *p;
    if (obj.IsJSObject() && !obj.IsJSFunction()) {
      PrintF("slot %p to %p\n", p.ToVoidPtr(),
             reinterpret_cast<void*>(obj.ptr()));
      obj.Print();
    }
  }

  void VisitRootPointers(Root root, const char* description,
                         FullObjectSlot start, FullObjectSlot end) override {
    for (FullObjectSlot p = start; p < end; ++p) {
      Object obj = *p;
      if (obj.IsJSObject() && !obj.IsJSFunction()) {
        PrintF("slot %p to %p\n", p.ToVoidPtr(),
               reinterpret_cast<void*>(obj.ptr()));
        obj.Print();
      }
    }
  }
};

class SnapshotCollector::RootMarkingVisitor final : public RootVisitor {
 public:
  explicit RootMarkingVisitor(SnapshotCollector* collector)
      : collector_(collector), is_shared_heap_(collector->is_shared_heap()) {}

  void VisitRootPointer(Root root, const char* description,
                        FullObjectSlot p) final {
    DCHECK(!MapWord::IsPacked(p.Relaxed_Load().ptr()));
    MarkObjectByPointer(root, p);
  }

  void VisitRootPointers(Root root, const char* description,
                         FullObjectSlot start, FullObjectSlot end) final {
    for (FullObjectSlot p = start; p < end; ++p) {
      MarkObjectByPointer(root, p);
    }
  }

  void VisitRunningCode(FullObjectSlot p) final {
    Code code = Code::cast(*p);

    // If Code is currently executing, then we must not remove its
    // deoptimization literals, which it might need in order to successfully
    // deoptimize.
    //
    // Must match behavior in RootsReferencesExtractor::VisitRunningCode, so
    // that heap snapshots accurately describe the roots.
    if (code.kind() != CodeKind::BASELINE) {
      DeoptimizationData deopt_data =
          DeoptimizationData::cast(code.deoptimization_data());
      if (deopt_data.length() > 0) {
        DeoptimizationLiteralArray literals = deopt_data.LiteralArray();
        int literals_length = literals.length();
        for (int i = 0; i < literals_length; ++i) {
          MaybeObject maybe_literal = literals.Get(i);
          HeapObject heap_literal;
          if (maybe_literal.GetHeapObject(&heap_literal)) {
            MarkObjectByPointer(Root::kStackRoots,
                                FullObjectSlot(&heap_literal));
          }
        }
      }
    }

    // And then mark the Code itself.
    VisitRootPointer(Root::kStackRoots, nullptr, p);
  }

 private:
  V8_INLINE void MarkObjectByPointer(Root root, FullObjectSlot p) {
    Object object = *p;
    if (!object.IsHeapObject()) return;
    HeapObject heap_object = HeapObject::cast(object);
    BasicMemoryChunk* target_page =
        BasicMemoryChunk::FromHeapObject(heap_object);
    if (is_shared_heap_ != target_page->InSharedHeap()) return;
    collector_->MarkRootObject(root, heap_object);
  }

  SnapshotCollector* const collector_;
  const bool is_shared_heap_;
};

class SnapshotMarkingVisitor {
 public:
  SnapshotMarkingVisitor(MarkingWorklists::Local* local_marking_worklists, Heap* heap)
      : local_marking_worklists_(local_marking_worklists),
        heap_(heap) {
  }

  void VisitMapPointer(HeapObject host) {

  }

  void VisitPointers(HeapObject host, ObjectSlot start, ObjectSlot end) {
    for (ObjectSlot slot = start; slot < end; ++slot) {
      Isolate* isolate = heap_->isolate();
      PtrComprCageBase cage_base(isolate);
      typename ObjectSlot::TObject object =
        slot.Relaxed_Load(cage_base);
      HeapObject heap_object;
      if (object.GetHeapObject(&heap_object)) {
        local_marking_worklists_->Push(heap_object);
        if (heap_object.IsJSObject() && !heap_object.IsJSFunction()) {
          PrintF("JS object %p pushed to worklist\n", reinterpret_cast<void*>(heap_object.ptr()));
          heap_object.Print();
        }
      }
    }
  }

 private:
  MarkingWorklists::Local* const local_marking_worklists_;
  Heap* const heap_;
};

SnapshotCollector::SnapshotCollector(Heap* heap)
    : isolate_(heap->isolate()),
      heap_(heap),
      is_shared_heap_(heap->IsShared()),
      marking_state_(heap->isolate()) {}

void SnapshotCollector::PrintRootObjects() {
  RootPrintVisitor print_visitor;

  heap_->IterateRoots(&print_visitor, base::EnumSet<SkipRoot>{SkipRoot::kWeak});
}

void SnapshotCollector::Prepare() {
  StartMarking();
}

void SnapshotCollector::StartMarking() {
  std::vector<Address> contexts =
      heap()->memory_measurement()->StartProcessing();
  
  marking_worklists()->CreateContextWorklists(contexts);

  auto* cpp_heap = CppHeap::From(heap_->cpp_heap());

  code_flush_mode_ = Heap::GetCodeFlushMode(isolate());

  local_marking_worklists_ = std::make_unique<MarkingWorklists::Local>(
      marking_worklists(),
      cpp_heap ? cpp_heap->CreateCppMarkingStateForMutatorThread()
               : MarkingWorklists::Local::kNoCppMarkingState);
  local_weak_objects_ = std::make_unique<WeakObjects::Local>(weak_objects());
  marking_visitor_ = std::make_unique<MarkingVisitor>(
      marking_state(), local_marking_worklists(), local_weak_objects_.get(),
      heap_, epoch(), code_flush_mode(),
      heap_->local_embedder_heap_tracer()->InUse(),
      heap_->ShouldCurrentGCKeepAgesUnchanged());
}

void SnapshotCollector::Finish() {
  local_marking_worklists_.reset();
  marking_worklists_.ReleaseContextWorklists();
}

void SnapshotCollector::CollectGarbage() {
  MarkLiveObjects();

  Finish();
}

void SnapshotCollector::MarkLiveObjects() {
  RootMarkingVisitor root_visitor(this);
  MarkRoots(&root_visitor);

  DrainMarkingWorklist();
}

void SnapshotCollector::MarkRoots(RootVisitor* root_visitor) {

  heap_->IterateRootsIncludingClients(root_visitor, base::EnumSet<SkipRoot>{SkipRoot::kWeak});
}

void SnapshotCollector::DrainMarkingWorklist() {
  HeapObject object;
  size_t bytes_processed = 0;
  size_t objects_processed = 0;
  //bool is_per_context_mode = local_marking_worklists()->IsPerContextMode();
  Isolate* isolate = heap()->isolate();
  PtrComprCageBase cage_base(isolate);
  while (local_marking_worklists()->Pop(&object) ||
         local_marking_worklists()->PopOnHold(&object)) {
    if (object.IsFreeSpaceOrFiller(cage_base)) {
      // Due to copying mark bits and the fact that grey and black have their
      // first bit set, one word fillers are always black.
      DCHECK_IMPLIES(object.map(cage_base) ==
                         ReadOnlyRoots(isolate).one_pointer_filler_map(),
                     marking_state()->IsBlack(object));
      // Other fillers may be black or grey depending on the color of the object
      // that was trimmed.
      DCHECK_IMPLIES(object.map(cage_base) !=
                         ReadOnlyRoots(isolate).one_pointer_filler_map(),
                     marking_state()->IsBlackOrGrey(object));
      continue;
    }

    DCHECK(object.IsHeapObject());
    DCHECK(heap()->Contains(object));
    // DCHECK(!(marking_state()->IsWhite(object)));
    
    // if (object.IsJSObject() && !object.IsJSFunction()) {
    //   PrintF("JS object %p poped from worklist\n", reinterpret_cast<void*>(object.ptr()));
    //   SnapshotMarkingVisitor visitor(local_marking_worklists_.get(), heap());
    //   Map map = object.map(cage_base);
    //   int size = JSObject::BodyDescriptor::SizeOf(map, object);
    //   JSObject::FastBodyDescriptor::IterateBody(map, object, size, &visitor);
    // }

    Map map = object.map(cage_base);
    size_t visited_size = marking_visitor_->Visit(map, object);

    bytes_processed += visited_size;
    objects_processed++;
  }

  PrintF("bytes_processed: %zu, object_processed: %zu", bytes_processed, objects_processed);
}

void SnapshotCollector::MarkRootObject(Root root, HeapObject obj) {
  if (marking_state()->WhiteToGrey(obj)) {
    local_marking_worklists()->Push(obj);
    if (V8_UNLIKELY(FLAG_track_retaining_path)) {
      heap_->AddRetainingRoot(root, obj);
    }
    if (obj.IsJSObject() && !obj.IsJSFunction()) {
      obj.Print();
    }
  }
}

} // namespace internal
} // namespace v8
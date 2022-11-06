#include "src/heap/snapshot-collector.h"

#include "src/objects/visitors.h"
#include "src/objects/objects.h"

namespace v8 {
namespace internal {

class PrintVisitor : public RootVisitor {
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

SnapshotCollector::SnapshotCollector(Heap* heap)
    : isolate_(heap->isolate()),
      heap_(heap),
      is_shared_heap_(heap->IsShared()) {}

void SnapshotCollector::PrintRootObjects() {
  PrintVisitor print_visitor;

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

  local_marking_worklists_ = std::make_unique<MarkingWorklists::Local>(
      marking_worklists(),
      cpp_heap ? cpp_heap->CreateCppMarkingStateForMutatorThread()
               : MarkingWorklists::Local::kNoCppMarkingState);
}

void SnapshotCollector::CollectGarbage() {
  MarkRoots();
}

void SnapshotCollector::MarkRoots() {
  RootMarkingVisitor rootVisitor(this);

  heap_->IterateRoots(&rootVisitor, base::EnumSet<SkipRoot>{SkipRoot::kWeak});
}

void SnapshotCollector::MarkRootObject(Root root, HeapObject obj) {
  local_marking_worklists()->Push(obj);
  if (obj.IsJSObject() && !obj.IsJSFunction()) {
    obj.Print();
  }
}

} // namespace internal
} // namespace v8
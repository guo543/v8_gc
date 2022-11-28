#include "include/v8-internal.h"
#include "src/heap/base/worklist.h"
#include "src/heap/concurrent-marking.h"
#include "src/heap/marking-visitor-inl.h"
#include "src/heap/marking-worklist.h"
#include "src/heap/marking.h"
#include "src/heap/memory-measurement.h"
#include "src/heap/parallel-work-item.h"
#include "src/heap/spaces.h"
#include "src/heap/sweeper.h"

namespace v8 {
namespace internal {

template <typename MarkingState>
class SnapshotMainMarkingVisitor final
    : public MarkingVisitorBase<SnapshotMainMarkingVisitor<MarkingState>,
                                MarkingState> {
 public:
  // This is used for revisiting objects that were black allocated.
  class V8_NODISCARD RevisitScope {
   public:
    explicit RevisitScope(SnapshotMainMarkingVisitor* visitor) : visitor_(visitor) {
      DCHECK(!visitor->revisiting_object_);
      visitor->revisiting_object_ = true;
    }
    ~RevisitScope() {
      DCHECK(visitor_->revisiting_object_);
      visitor_->revisiting_object_ = false;
    }

   private:
    SnapshotMainMarkingVisitor<MarkingState>* visitor_;
  };

  SnapshotMainMarkingVisitor(MarkingState* marking_state,
                             MarkingWorklists::Local* local_marking_worklists,
                             WeakObjects::Local* local_weak_objects, Heap* heap,
                             unsigned mark_compact_epoch,
                             base::EnumSet<CodeFlushMode> code_flush_mode,
                             bool embedder_tracing_enabled,
                             bool should_keep_ages_unchanged)
      : MarkingVisitorBase<SnapshotMainMarkingVisitor<MarkingState>, MarkingState>(
            local_marking_worklists, local_weak_objects, heap,
            mark_compact_epoch, code_flush_mode, embedder_tracing_enabled,
            should_keep_ages_unchanged),
        marking_state_(marking_state),
        revisiting_object_(false) {}

  // HeapVisitor override to allow revisiting of black objects.
  bool ShouldVisit(HeapObject object) {
    return marking_state_->GreyToBlack(object) ||
           V8_UNLIKELY(revisiting_object_);
  }

 private:
  // Functions required by MarkingVisitorBase.

  template <typename T, typename TBodyDescriptor = typename T::BodyDescriptor>
  int VisitJSObjectSubclass(Map map, T object) {
    if (!this->ShouldVisit(object)) return 0;
    this->VisitMapPointer(object);
    int size = TBodyDescriptor::SizeOf(map, object);
    TBodyDescriptor::IterateBody(map, object, size, this);
    return size;
  }

  template <typename T>
  int VisitLeftTrimmableArray(Map map, T object) {
    if (!this->ShouldVisit(object)) return 0;
    int size = T::SizeFor(object.length());
    this->VisitMapPointer(object);
    T::BodyDescriptor::IterateBody(map, object, size, this);
    return size;
  }

  template <typename TSlot>
  void RecordSlot(HeapObject object, TSlot slot, HeapObject target) {
    MarkCompactCollector::RecordSlot(object, slot, target);
  }

  void RecordRelocSlot(Code host, RelocInfo* rinfo, HeapObject target) {
    MarkCompactCollector::RecordRelocSlot(host, rinfo, target);
  }

  void SynchronizePageAccess(HeapObject heap_object) {
    // Nothing to do on the main thread.
  }

  MarkingState* marking_state() { return marking_state_; }

  TraceRetainingPathMode retaining_path_mode() {
    return (V8_UNLIKELY(FLAG_track_retaining_path))
               ? TraceRetainingPathMode::kEnabled
               : TraceRetainingPathMode::kDisabled;
  }

  MarkingState* const marking_state_;

  friend class MarkingVisitorBase<SnapshotMainMarkingVisitor<MarkingState>,
                                  MarkingState>;
  bool revisiting_object_;
};

class SnapshotCollector {
 public:
  class RootMarkingVisitor;
  using MarkingState = MajorMarkingState;
  using MarkingVisitor = SnapshotMainMarkingVisitor<MarkingState>;

  explicit SnapshotCollector(Heap* heap);

  void Prepare();

  void CollectGarbage();

  inline Heap* heap() { return heap_; }
  inline bool is_shared_heap() const { return is_shared_heap_; }

  inline MarkingState* marking_state() { return &marking_state_; }
  
  MarkingWorklists* marking_worklists() { return &marking_worklists_; }
  MarkingWorklists::Local* local_marking_worklists() {
    return local_marking_worklists_.get();
  }

  WeakObjects* weak_objects() { return &weak_objects_; }
  WeakObjects::Local* local_weak_objects() { return local_weak_objects_.get(); }

  unsigned epoch() const { return epoch_; }

  base::EnumSet<CodeFlushMode> code_flush_mode() const {
    return code_flush_mode_;
  }

  Isolate* isolate() { return isolate_; }

 private:
  void PrintRootObjects();

  void StartMarking();
  void Finish();

  void MarkLiveObjects();

  void MarkRoots(RootVisitor* root_visitor);
  void MarkRootObject(Root root, HeapObject obj);

  void DrainMarkingWorklist();

  Isolate* const isolate_;
  Heap* const heap_;

  bool is_shared_heap_;

  unsigned epoch_ = 0;

  MarkingWorklists marking_worklists_;
  WeakObjects weak_objects_;

  std::unique_ptr<MarkingVisitor> marking_visitor_;
  std::unique_ptr<MarkingWorklists::Local> local_marking_worklists_;
  std::unique_ptr<WeakObjects::Local> local_weak_objects_;

  MarkingState marking_state_;

  base::EnumSet<CodeFlushMode> code_flush_mode_;
};

} // namespace internal
} // namespace v8
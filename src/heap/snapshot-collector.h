#include "src/heap/heap-inl.h"

namespace v8 {
namespace internal {

class SnapshotCollector {
 public:
  class RootMarkingVisitor;
  using MarkingState = MajorMarkingState;

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

 private:
  void PrintRootObjects();

  void StartMarking();
  void Finish();

  void MarkRoots();
  void MarkRootObject(Root root, HeapObject obj);

  void DrainMarkingWorklist();

  Isolate* const isolate_;
  Heap* const heap_;

  bool is_shared_heap_;

  MarkingWorklists marking_worklists_;
  std::unique_ptr<MarkingWorklists::Local> local_marking_worklists_;

  MarkingState marking_state_;
};

} // namespace internal
} // namespace v8
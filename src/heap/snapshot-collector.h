#include "src/heap/heap-inl.h"

namespace v8 {
namespace internal {

class SnapshotCollector {
 public:
  class RootMarkingVisitor;

  explicit SnapshotCollector(Heap* heap);

  void PrintRootObjects();

  void Prepare();
  void StartMarking();

  void CollectGarbage();

  void MarkRoots();
  void MarkRootObject(Root root, HeapObject obj);

  inline Heap* heap() { return heap_; }
  inline bool is_shared_heap() const { return is_shared_heap_; }
  
  MarkingWorklists* marking_worklists() { return &marking_worklists_; }

  MarkingWorklists::Local* local_marking_worklists() {
    return local_marking_worklists_.get();
  }

 private:
  Isolate* const isolate_;
  Heap* const heap_;

  bool is_shared_heap_;

  MarkingWorklists marking_worklists_;
  std::unique_ptr<MarkingWorklists::Local> local_marking_worklists_;
};

} // namespace internal
} // namespace v8
#include "src/heap/heap-inl.h"

namespace v8 {
namespace internal {

class SnapshotCollector {
 public:
  explicit SnapshotCollector(Heap* heap);

  void PrintRootObjects();

 private:
  Isolate* const isolate_;
  Heap* const heap_;
};

} // namespace internal
} // namespace v8
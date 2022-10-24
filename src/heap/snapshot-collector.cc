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

SnapshotCollector::SnapshotCollector(Heap* heap)
    : isolate_(heap->isolate()), heap_(heap) {}

void SnapshotCollector::PrintRootObjects() {
  PrintVisitor print_visitor;

  heap_->IterateRoots(&print_visitor, base::EnumSet<SkipRoot>{SkipRoot::kWeak});
}

} // namespace internal
} // namespace v8
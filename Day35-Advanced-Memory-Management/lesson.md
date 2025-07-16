# Day 35: Advanced Memory Management

Understanding Python's memory model helps optimize performance and avoid leaks.

**Memory Management Techniques:**
- Reference counting (automatic)
- Garbage collection (circular references)
- `__slots__` for memory-efficient classes
- `weakref` for caches

**Memory Profiling Example:**
```python
import sys
import weakref

class Data:
    def __init__(self, value):
        self.value = value

d = Data(42)
print('Reference count:', sys.getrefcount(d) - 1)

# Weak reference doesn't prevent garbage collection
weak_d = weakref.ref(d)
print('Weak ref value:', weak_d().value)
```

---
**Pro Tip:**
Use `sys.getsizeof()` to check object size and `tracemalloc` for memory allocation tracking.

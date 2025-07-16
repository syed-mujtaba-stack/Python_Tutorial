# Day 19: C Extensions & Cython (Intro)

Python can be extended with C for performance-critical code. Cython makes it easier to write C-accelerated Python modules.

**C Extension Example:**
- Write C code and use Python’s `ctypes` or `cffi` to call it.

**Cython Example:**
```python
# example.pyx
cpdef int add(int a, int b):
    return a + b
```
- Compile with: `cythonize -i example.pyx`

---
**Pro Tip:**
Only use C/Cython for bottlenecks. Most Python code does not need C extensions!

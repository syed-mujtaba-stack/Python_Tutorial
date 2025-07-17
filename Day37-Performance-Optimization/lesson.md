# Day 37: Performance Optimization

Learn techniques to make your Python code run faster and use less memory.

**Performance Tips:**
1. Use built-in functions and libraries (written in C)
2. Optimize data structures (lists vs sets for lookups)
3. Use list comprehensions and generator expressions
4. Avoid global variables
5. Use `lru_cache` for expensive function calls

**Profiling Example:**
```python
import cProfile

def slow_function():
    return sum(i * 2 for i in range(10**6))

# Profile the function
cProfile.run('slow_function()')
```

**Optimizing with NumPy:**
```python
import numpy as np

def numpy_version():
    arr = np.arange(10**6)
    return np.sum(arr * 2)
```

---
**Pro Tip:**
Always measure before optimizing. Use `timeit` for microbenchmarks and `cProfile` for detailed profiling.

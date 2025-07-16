# Day 18: Profiling & Optimization

Profiling helps you find bottlenecks in your code. Python provides tools like `cProfile`, `timeit`, and memory profilers.

**cProfile Example:**
```python
import cProfile
def slow_func():
    sum = 0
    for i in range(100000):
        sum += i
    return sum
cProfile.run('slow_func()')
```

**timeit Example:**
```python
import timeit
print(timeit.timeit('sum(range(1000))', number=10000))
```

---
**Pro Tip:**
Optimize only after measuring. Use profiling data to target the slowest parts of your code.

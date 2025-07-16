# Day 22: Advanced itertools & functools

Python’s `itertools` and `functools` modules provide powerful tools for functional and iterator-based programming.

**itertools Example:**
```python
import itertools
for x in itertools.cycle([1, 2, 3]):
    print(x)
    break  # Remove break for infinite cycle
```

**functools Example:**
```python
from functools import lru_cache
@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))
```

---
**Pro Tip:**
Use `itertools` for efficient looping, and `functools` for decorators, caching, and partial functions.

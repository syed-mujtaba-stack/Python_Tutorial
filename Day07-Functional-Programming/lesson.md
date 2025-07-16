# Day 7: Functional Programming in Python

Functional programming emphasizes immutability and stateless functions. Python supports functional tools like `map`, `filter`, `reduce`, and `lambda`.

**Examples:**
```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
```

**Useful Modules:**
- `functools`
- `itertools`

---
**Pro Tip:**
Prefer comprehensions for readability, but use `map`, `filter`, and `reduce` for concise, functional code.

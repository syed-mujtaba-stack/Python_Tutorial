# Day 31: Advanced Data Structures

Python offers powerful data structures beyond lists and dictionaries. Let's explore advanced ones from the `collections` module and beyond.

**DefaultDict Example:**
```python
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1  # No KeyError!
```

**Counter Example:**
```python
from collections import Counter
c = Counter('hello')
print(c)  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
```

**Deque Example:**
```python
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)  # Efficient left append
```

---
**Pro Tip:**
Use `defaultdict` for handling missing keys, `Counter` for counting, and `deque` for fast appends/pops from both ends.

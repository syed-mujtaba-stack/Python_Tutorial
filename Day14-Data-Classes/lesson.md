# Day 14: Data Classes & NamedTuples

Data classes (Python 3.7+) provide a simple way to create classes for storing data. NamedTuples are immutable, lightweight alternatives.

**Data Class Example:**
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(2, 3)
print(p)
```

**NamedTuple Example:**
```python
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
p = Person('Ali', 30)
print(p.name, p.age)
```

---
**Pro Tip:**
Use data classes for mutable records, and NamedTuples for lightweight, immutable data.

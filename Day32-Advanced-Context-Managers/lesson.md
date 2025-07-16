# Day 32: Advanced Context Managers

Context managers help manage resources and setup/teardown operations. You can create them using classes or the `contextlib` module.

**Class-based Context Manager:**
```python
class MyContext:
    def __enter__(self):
        print('Entering context')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting context')

with MyContext() as ctx:
    print('Inside context')
```

**contextlib Example:**
```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print('Entering')
    yield 'Hello'
    print('Exiting')

with my_context() as value:
    print('Inside:', value)
```

---
**Pro Tip:**
Use context managers for resource cleanup, locks, and any setup/teardown operations.

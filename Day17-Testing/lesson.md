# Day 17: Testing in Python (unittest, pytest, mocking)

Testing ensures your code works as expected and prevents regressions. Python’s built-in `unittest` and popular `pytest` frameworks make testing easy. Mocking lets you simulate dependencies.

**unittest Example:**
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

**pytest Example:**
```python
def test_add():
    assert add(2, 3) == 5
```

---
**Pro Tip:**
Use mocking (`unittest.mock`) to isolate units of code and test in isolation.

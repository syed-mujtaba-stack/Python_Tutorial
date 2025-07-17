# Day 40: Advanced Testing Strategies

Learn professional testing techniques to ensure code quality and reliability.

**Testing with pytest:**
```python
# test_operations.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

**Fixtures for Test Setup:**
```python
import pytest

@pytest.fixture
db_connection():
    # Setup code
    conn = create_db_connection()
    yield conn  # This is where testing happens
    # Teardown code
    conn.close()

def test_database(db_connection):
    result = db_connection.query("SELECT 1")
    assert result == 1
```

**Parameterized Tests:**
```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(a, b, expected):
    assert a + b == expected
```

---
**Pro Tip:**
Follow the AAA pattern: Arrange-Act-Assert for clear test structure.

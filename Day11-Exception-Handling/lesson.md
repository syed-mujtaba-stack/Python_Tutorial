# Day 11: Advanced Exception Handling

Python’s exception system allows for robust error handling and debugging. Advanced techniques include custom exceptions, exception chaining, and using `else`/`finally`.

**Custom Exception Example:**
```python
class MyError(Exception):
    pass

try:
    raise MyError('Something went wrong!')
except MyError as e:
    print('Caught:', e)
```

**Exception Chaining:**
```python
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError('Bad math!') from e
```

**Pro Tip:**
Use `finally` for cleanup, and always inherit custom exceptions from `Exception`.

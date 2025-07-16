# Day 1: Closures & Decorators

## Closures
A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

**Example:**
```python
def outer(msg):
    def inner():
        print(msg)
    return inner

closure_func = outer('Hello, Closure!')
closure_func()  # Output: Hello, Closure!
```

## Decorators
Decorators are functions that modify the behavior of other functions. They are widely used for logging, access control, timing, etc.

**Example:**
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before function call')
        result = func(*args, **kwargs)
        print('After function call')
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f'Hello, {name}!')

greet('Python')
```

---
**Pro Tip:**
Use `functools.wraps` to preserve metadata of the original function when writing decorators.

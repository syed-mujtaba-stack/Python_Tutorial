# Day 33: Advanced Decorators

Decorators are a powerful Python feature for modifying or enhancing functions. Let's explore advanced patterns.

**Decorator with Arguments:**
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f'Hello {name}!')
```

**Class-based Decorator:**
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'Call {self.calls} of {self.func.__name__}')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello!')
```

---
**Pro Tip:**
Use `functools.wraps` to preserve function metadata in decorators.

# Day 1 Solution: Closures & Decorators
from functools import wraps

# 1. Closure for multiplier
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

mul_by_3 = make_multiplier(3)
print('3 x 5 =', mul_by_3(5))  # Output: 15

# 2. Logging decorator
def log_args_and_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        print(f'Result: {result}')
        return result
    return wrapper

@log_args_and_result
def add(a, b):
    return a + b

add(4, 7)  # Logs arguments and result

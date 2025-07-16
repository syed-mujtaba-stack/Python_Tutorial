# Day 33 Script: Advanced Decorators Demo
from functools import wraps
import time

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start:.2f}s')
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return 'Done'

slow_function()

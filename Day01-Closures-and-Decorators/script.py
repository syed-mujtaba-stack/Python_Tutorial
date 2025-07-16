# Day 1 Script: Closures & Decorators Demo
from functools import wraps

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@timer_decorator
def compute_sum(n):
    return sum(range(n))

print('Sum:', compute_sum(1000000))

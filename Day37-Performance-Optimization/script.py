# Day 37 Script: Performance Optimization Demo
from functools import lru_cache
import time

# 1. Memoization with lru_cache
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 2. List vs Generator memory usage
def get_numbers_list(n):
    return [i for i in range(n)]

def get_numbers_gen(n):
    return (i for i in range(n))

# 3. String concatenation optimization
def slow_concat():
    s = ""
    for i in range(10000):
        s += str(i)
    return s

def fast_concat():
    return "".join(str(i) for i in range(10000))

# Time the functions
print("Fibonacci(35) with caching:", timeit.timeit(lambda: fibonacci(35), number=1))
print("List vs Generator memory:")
print("- List size:", sum(1 for _ in get_numbers_list(1000000)))  # Uses memory
print("- Generator size:", sum(1 for _ in get_numbers_gen(1000000)))  # Memory efficient

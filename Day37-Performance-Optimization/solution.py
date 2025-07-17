# Day 37 Solution: Performance Optimization
import timeit
import numpy as np

def sum_of_squares_slow(n):
    result = 0
    for i in range(n):
        result += i ** 2
    return result

def sum_of_squares_fast(n):
    # Using sum with generator expression
    return sum(i ** 2 for i in range(n))

def sum_of_squares_numpy(n):
    # Using NumPy for vectorized operations
    return np.sum(np.arange(n) ** 2)

# Benchmarking
n = 10**6
print("Original:", timeit.timeit(lambda: sum_of_squares_slow(n), number=10))
print("Optimized:", timeit.timeit(lambda: sum_of_squares_fast(n), number=10))
print("NumPy:", timeit.timeit(lambda: sum_of_squares_numpy(n), number=10))

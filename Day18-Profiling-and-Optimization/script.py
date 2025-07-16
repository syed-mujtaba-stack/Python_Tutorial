# Day 18 Script: Profiling & Optimization Demo
import timeit

def list_comp():
    return [x*x for x in range(10000)]

def loop():
    res = []
    for x in range(10000):
        res.append(x*x)
    return res

print('List comprehension:', timeit.timeit(list_comp, number=100))
print('For loop:', timeit.timeit(loop, number=100))

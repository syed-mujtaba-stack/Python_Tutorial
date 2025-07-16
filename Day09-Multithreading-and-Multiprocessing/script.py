# Day 9 Script: Multithreading & Multiprocessing Demo
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def square(x):
    time.sleep(0.2)
    return x * x

with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(square, [1, 2, 3]))
    print('ThreadPool results:', results)

with ProcessPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(square, [4, 5, 6]))
    print('ProcessPool results:', results)

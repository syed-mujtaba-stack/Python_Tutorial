# Day 32 Solution: Advanced Context Managers
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'Time taken: {end - start:.2f}s')

# Usage:
with timer():
    time.sleep(1)  # Simulate work

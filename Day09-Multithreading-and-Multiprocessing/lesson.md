# Day 9: Multithreading & Multiprocessing in Python

Python supports concurrency using threads and processes. Use threads for I/O-bound tasks and processes for CPU-bound tasks.

**Multithreading Example:**
```python
import threading

def print_numbers():
    for i in range(5):
        print('Thread:', i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

**Multiprocessing Example:**
```python
from multiprocessing import Process

def show_pid():
    import os
    print('Process ID:', os.getpid())

p = Process(target=show_pid)
p.start()
p.join()
```

---
**Pro Tip:**
Use `concurrent.futures` for high-level thread and process pools.

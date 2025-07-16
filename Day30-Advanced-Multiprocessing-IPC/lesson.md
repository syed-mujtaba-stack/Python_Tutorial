# Day 30: Advanced Multiprocessing & Inter-Process Communication (IPC)

Python’s `multiprocessing` module allows true parallelism. For complex workflows, you may need process pools, queues, pipes, or shared memory.

**Process Pool Example:**
```python
from multiprocessing import Pool
def square(x):
    return x * x
with Pool(4) as p:
    print(p.map(square, [1, 2, 3, 4]))
```

**Queue Example:**
```python
from multiprocessing import Process, Queue
def f(q):
    q.put([42, None, 'hello'])
q = Queue()
p = Process(target=f, args=(q,))
p.start()
print(q.get())
p.join()
```

---
**Pro Tip:**
Use queues and pipes for safe communication between processes. Consider `concurrent.futures.ProcessPoolExecutor` for simpler cases.

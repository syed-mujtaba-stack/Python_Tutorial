# Day 30 Solution: Advanced Multiprocessing & IPC
from multiprocessing import Pool, Process, Queue

def cube(x):
    return x ** 3

with Pool(2) as p:
    print('Cubes:', p.map(cube, [1, 2, 3, 4]))

def send(q):
    q.put('Hello from process!')

q = Queue()
p = Process(target=send, args=(q,))
p.start()
print('Received:', q.get())
p.join()

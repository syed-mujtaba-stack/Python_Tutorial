# Day 35 Script: Advanced Memory Management Demo
import tracemalloc
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Circular reference
a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Circular reference

# Garbage collection
gc.collect()
print('Garbage collection:', gc.garbage)

# Memory tracking
tracemalloc.start()
data = [1] * 1000
current, peak = tracemalloc.get_traced_memory()
print(f'Current memory: {current / 1024:.2f} KB')
print(f'Peak memory: {peak / 1024:.2f} KB')
tracemalloc.stop()

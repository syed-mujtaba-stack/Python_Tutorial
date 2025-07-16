# Day 2: Generators & Iterators

Generators and iterators provide a memory-efficient way to work with large data streams in Python.

## Iterators
Any object with `__iter__()` and `__next__()` methods is an iterator.

**Example:**
```python
nums = iter([1, 2, 3])
print(next(nums))  # 1
print(next(nums))  # 2
```

## Generators
Generators are a simple way to create iterators using functions and the `yield` keyword.

**Example:**
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)
```

---
**Pro Tip:**
Generators are ideal for processing large files, infinite sequences, or streams without loading everything into memory.

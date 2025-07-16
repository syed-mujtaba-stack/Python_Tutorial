# Day 24: Advanced File I/O & Binary Data

Python supports advanced file operations, including binary files, buffering, and memory mapping.

**Binary File Example:**
```python
with open('data.bin', 'wb') as f:
    f.write(b'\x00\xFF')

with open('data.bin', 'rb') as f:
    data = f.read()
    print(data)
```

**Memory Mapping Example:**
```python
import mmap
with open('data.bin', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm[:])
    mm.close()
```

---
**Pro Tip:**
Use binary mode ('rb', 'wb') for non-text files. Memory mapping is efficient for large files.

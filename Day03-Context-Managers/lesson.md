# Day 3: Context Managers (`with` Statement)

Context managers automate setup and cleanup actions, most commonly used with files, network connections, and locks. The `with` statement ensures resources are managed safely.

**Example:**
```python
with open('example.txt', 'w') as f:
    f.write('Hello, context managers!')
```

You can create custom context managers using classes or the `contextlib` module.

**Custom Context Manager (class-based):**
```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with ManagedFile('test.txt') as f:
    f.write('Using a custom context manager!')
```

**Pro Tip:**
Use `contextlib.contextmanager` for simpler context managers using generator syntax.

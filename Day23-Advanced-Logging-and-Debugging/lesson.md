# Day 23: Advanced Logging & Debugging

Logging and debugging are critical for professional software. Python’s `logging` module and debuggers like `pdb` make this easy.

**Logging Example:**
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info('This is an info message')
```

**Debugger Example:**
```python
import pdb
pdb.set_trace()
# Execution pauses here for interactive debugging
```

---
**Pro Tip:**
Use logging for production, print for quick checks, and debuggers for complex bugs.

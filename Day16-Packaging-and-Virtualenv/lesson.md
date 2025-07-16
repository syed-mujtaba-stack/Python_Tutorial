# Day 16: Packaging & Virtual Environments

Packaging lets you distribute Python code as reusable modules. Virtual environments isolate dependencies for each project.

**Virtualenv Example:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Basic `setup.py` Example:**
```python
from setuptools import setup
setup(
    name='my_package',
    version='0.1',
    py_modules=['my_module'],
)
```

---
**Pro Tip:**
Always use a virtual environment for every project and include a `requirements.txt`.

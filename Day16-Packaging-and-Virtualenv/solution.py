# Day 16 Solution: Packaging & Virtualenv
# (1) Virtual environment commands (run in terminal):
# python -m venv venv
# source venv/bin/activate  # On Windows: venv\Scripts\activate

# (2) Minimal setup.py
from setuptools import setup
setup(
    name='demo_package',
    version='0.1',
    py_modules=['demo_module'],
)

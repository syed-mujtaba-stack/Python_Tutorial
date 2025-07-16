# Day 32 Script: Advanced Context Managers Demo
from contextlib import contextmanager

@contextmanager
def suppress_errors():
    try:
        yield
    except Exception as e:
        print(f'Suppressed error: {e}')

# Usage:
with suppress_errors():
    print(1 / 0)  # Error will be caught and suppressed

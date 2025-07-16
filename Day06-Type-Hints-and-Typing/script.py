# Day 6 Script: Type Hints & Typing Demo
from typing import Optional

def safe_divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b

result = safe_divide(10, 2)
print('Result:', result)
result = safe_divide(10, 0)
print('Result:', result)

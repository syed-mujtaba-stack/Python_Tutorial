# Day 6: Type Hints & Typing Module

Type hints improve code readability and help catch errors early. The `typing` module provides advanced types.

**Basic Example:**
```python
def greet(name: str) -> str:
    return f'Hello, {name}'
```

**Advanced Types:**
```python
from typing import List, Dict, Optional, Union

def process(items: List[int]) -> Dict[str, int]:
    return {'count': len(items)}

def maybe_int(x: Optional[int]) -> int:
    return x if x is not None else 0

def add(x: int, y: Union[int, float]) -> float:
    return x + y
```

---
**Pro Tip:**
Use `mypy` for static type checking in your projects.

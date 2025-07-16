# Day 28: Advanced Unittesting & Mocking

Professional Python projects require robust testing. Go beyond basics with test discovery, fixtures, and mocking using `unittest.mock`.

**Mocking Example:**
```python
from unittest.mock import patch
import requests

def get_status(url):
    resp = requests.get(url)
    return resp.status_code

with patch('requests.get') as mock_get:
    mock_get.return_value.status_code = 200
    print(get_status('http://example.com'))  # Output: 200
```

**Test Discovery:**
- `python -m unittest discover`

---
**Pro Tip:**
Mock external APIs and databases to make your tests fast and reliable.

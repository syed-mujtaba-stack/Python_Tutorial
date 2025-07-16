# Day 12: Regular Expressions (re module)

Regular expressions (regex) are used for powerful text searching, matching, and manipulation. Python’s `re` module provides full regex support.

**Basic Example:**
```python
import re
pattern = r'\d+'
text = 'There are 42 apples.'
match = re.search(pattern, text)
if match:
    print('Found:', match.group())  # Output: 42
```

**Common Functions:**
- `re.match`, `re.search`, `re.findall`, `re.sub`

---
**Pro Tip:**
Use raw strings (`r''`) for regex patterns to avoid escaping issues.

# Day 29: Advanced Serialization & Pickling

Serialization is the process of converting objects to a format that can be saved or transmitted. Python supports several serialization formats, with `pickle` being the most flexible for Python objects.

**Pickle Example:**
```python
import pickle
data = {'a': 1, 'b': 2}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
    print(loaded)
```

**Warning:**
Never unpickle data from untrusted sources (security risk).

---
**Pro Tip:**
Use `json` for cross-language compatibility, `pickle` for Python-specific objects.

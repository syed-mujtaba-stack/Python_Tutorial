# Day 26: Advanced JSON, YAML, TOML Handling

Python supports multiple serialization formats for data exchange and configuration: JSON (standard), YAML (human-friendly), TOML (config files).

**JSON Example:**
```python
import json
data = {'x': 1, 'y': 2}
with open('data.json', 'w') as f:
    json.dump(data, f)
```

**YAML Example:**
```python
import yaml
with open('data.yaml', 'w') as f:
    yaml.dump(data, f)
```

**TOML Example:**
```python
import toml
toml_str = toml.dumps(data)
with open('data.toml', 'w') as f:
    f.write(toml_str)
```

---
**Pro Tip:**
YAML and TOML require third-party packages: `PyYAML`, `toml`.

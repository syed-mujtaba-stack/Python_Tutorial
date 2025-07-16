# Day 26 Solution: Advanced JSON, YAML, TOML
import yaml

data = {'a': 10, 'b': 20}
with open('my.yaml', 'w') as f:
    yaml.dump(data, f)

with open('my.yaml') as f:
    loaded = yaml.safe_load(f)
    print(loaded)

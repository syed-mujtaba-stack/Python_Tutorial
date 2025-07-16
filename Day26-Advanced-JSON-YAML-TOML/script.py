# Day 26 Script: Advanced JSON, YAML, TOML Demo
import toml

data = {'project': {'name': 'Demo', 'version': '1.0'}}
with open('demo.toml', 'w') as f:
    f.write(toml.dumps(data))

with open('demo.toml') as f:
    print(f.read())

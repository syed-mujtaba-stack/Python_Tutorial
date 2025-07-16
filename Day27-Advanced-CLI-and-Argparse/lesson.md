# Day 27: Advanced CLI Apps & argparse

Python makes it easy to build professional command-line tools using the `argparse` module (standard) and third-party tools like `click`.

**argparse Example:**
```python
import argparse
parser = argparse.ArgumentParser(description='Demo CLI')
parser.add_argument('--name', type=str, help='Your name')
args = parser.parse_args()
print('Hello,', args.name)
```

**click Example:**
```python
import click
@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.argument('name')
def hello(count, name):
    for _ in range(count):
        print(f'Hello, {name}!')
# if __name__ == '__main__':
#     hello()
```

---
**Pro Tip:**
Use `argparse` for simple tools, `click` for more advanced CLI apps.

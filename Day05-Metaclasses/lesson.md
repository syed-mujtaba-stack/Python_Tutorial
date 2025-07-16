# Day 5: Metaclasses in Python

Metaclasses are the 'classes of classes'. They allow you to control class creation, add attributes, or enforce rules. Advanced, but powerful for frameworks and libraries.

**Basic Example:**
```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class {name}')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass
# Output: Creating class MyClass
```

**Use Cases:**
- Auto-registering classes
- Enforcing coding standards
- Injecting methods/attributes

---
**Pro Tip:**
Use metaclasses only when necessary. Most advanced Python code can be written without them.

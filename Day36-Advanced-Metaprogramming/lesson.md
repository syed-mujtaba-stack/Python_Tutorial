# Day 36: Advanced Metaprogramming

Metaprogramming allows you to write code that manipulates code. Python provides powerful tools for this.

**Metaclass Example:**
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by'] = 'MetaClass'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.created_by)  # 'MetaClass'
```

**Dynamic Class Creation:**
```python
MyClass = type('MyClass', (), {'x': 42})
print(MyClass().x)  # 42
```

**Attribute Access Control:**
```python
class Data:
    def __init__(self):
        self._data = {}
    
    def __getattr__(self, name):
        return self._data.get(name, 0)
    
    def __setattr__(self, name, value):
        if name == '_data':
            super().__setattr__(name, value)
        else:
            self._data[name] = value * 2

d = Data()
d.x = 21
print(d.x)  # 42
```

---
**Pro Tip:**
Use metaprogramming judiciously - it can make code harder to understand if overused.

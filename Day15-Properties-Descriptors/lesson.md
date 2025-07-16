# Day 15: Properties, Setters, Getters, and Descriptors

Python’s property system allows you to control attribute access with getter/setter methods. Descriptors provide even more control for advanced use cases.

**Property Example:**
```python
class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Name cannot be empty')
        self._name = value

p = Person('Ali')
p.name = 'Sara'
print(p.name)
```

**Descriptor Example:**
```python
class UpperCaseDescriptor:
    def __get__(self, instance, owner):
        return instance._value.upper()
    def __set__(self, instance, value):
        instance._value = value

class Demo:
    value = UpperCaseDescriptor()
    def __init__(self, value):
        self._value = value

obj = Demo('hello')
print(obj.value)  # Output: HELLO
```

---
**Pro Tip:**
Use properties for encapsulation and validation, descriptors for reusable attribute logic.

# Day 4: Advanced OOP – Multiple Inheritance, Mixins, and Abstract Base Classes

Python supports multiple inheritance, allowing a class to inherit from more than one parent. Mixins are a pattern for reusable functionality. Abstract Base Classes (ABCs) define interfaces and enforce method implementation.

**Multiple Inheritance Example:**
```python
class A: pass
class B: pass
class C(A, B): pass
```

**Mixin Example:**
```python
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Person(JsonMixin):
    def __init__(self, name):
        self.name = name

p = Person('Ali')
print(p.to_json())
```

**Abstract Base Class Example:**
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('Woof!')
```

---
**Pro Tip:**
Use ABCs for enforcing contracts, and mixins for code reuse without inheritance chains.

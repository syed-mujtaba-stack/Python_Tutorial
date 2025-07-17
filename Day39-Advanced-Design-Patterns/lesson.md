# Day 39: Advanced Design Patterns

Design patterns are reusable solutions to common problems in software design.

**Singleton Pattern:**
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

**Observer Pattern:**
```python
class Observable:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

class Observer:
    def update(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'from', observable)
```

**Factory Pattern:**
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    pets = {"dog": Dog(), "cat": Cat()}
    return pets[pet]
```

---
**Pro Tip:**
Use design patterns to make your code more flexible, reusable, and maintainable.

# Day 25: Metaprogramming & Reflection

Metaprogramming lets you write code that manipulates code! Reflection allows inspection and modification at runtime.

**Reflection Example:**
```python
class Foo:
    def bar(self):
        pass
obj = Foo()
print(type(obj))
print(dir(obj))
print(hasattr(obj, 'bar'))
```

**Dynamic Attribute Example:**
```python
setattr(obj, 'baz', 123)
print(obj.baz)
```

**Metaclass Recap:**
- Classes are objects too! Use `type` or custom metaclasses to control class creation.

---
**Pro Tip:**
Use reflection for plugins, serialization, and frameworks. Use metaclasses sparingly!

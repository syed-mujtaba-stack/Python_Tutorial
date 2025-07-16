# Day 35 Solution: Advanced Memory Management
import sys
import weakref

# 1. __slots__ memory comparison
class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlotsClass:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 2. Weakref cache
class Cache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    
    def store(self, key, value):
        self._cache[key] = value
    
    def get(self, key):
        return self._cache.get(key)

# Memory comparison
print('Regular class size:', sys.getsizeof(RegularClass(1, 2)))
print('Slots class size:', sys.getsizeof(SlotsClass(1, 2)))

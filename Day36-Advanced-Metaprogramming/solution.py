# Day 36 Solution: Advanced Metaprogramming
class Versioned(type):
    def __new__(cls, name, bases, namespace):
        namespace['version'] = '1.0'
        return super().__new__(cls, name, bases, namespace)

class LazyLoader:
    def __init__(self):
        self._data = {}
    
    def __getattr__(self, name):
        if name not in self._data:
            print(f'Loading {name}...')
            self._data[name] = f'Data for {name}'
        return self._data[name]

# Test metaclass
class MyClass(metaclass=Versioned):
    pass

print('Version:', MyClass.version)

# Test lazy loading
loader = LazyLoader()
print(loader.user_profile)  # Loads on first access
print(loader.user_profile)  # Uses cached version

# Day 36 Script: Advanced Metaprogramming Demo
class AutoRegister(type):
    registry = {}
    
    def __new__(cls, name, bases, namespace):
        new_class = super().__new__(cls, name, bases, namespace)
        if name != 'BasePlugin':
            cls.registry[name.lower()] = new_class
        return new_class

# Plugin system using metaclass
class BasePlugin(metaclass=AutoRegister):
    @classmethod
    def run(cls):
        return f"Running {cls.__name__}"

class PluginA(BasePlugin):
    pass

class PluginB(BasePlugin):
    pass

# All plugins are automatically registered
print("Available plugins:", list(AutoRegister.registry.keys()))
print(PluginA.run())  # Running PluginA

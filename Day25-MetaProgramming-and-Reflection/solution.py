# Day 25 Solution: Metaprogramming & Reflection

def print_attrs(obj):
    for attr in dir(obj):
        print(attr)

class MyClass:
    pass

def new_method(self):
    print('Dynamic method!')

MyClass.dynamic = new_method
obj = MyClass()
obj.dynamic()

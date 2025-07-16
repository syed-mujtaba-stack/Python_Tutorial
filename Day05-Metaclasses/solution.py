# Day 5 Solution: Metaclasses

class PrintNameMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class: {name}')
        return super().__new__(cls, name, bases, dct)

class Foo(metaclass=PrintNameMeta):
    pass

class Bar(metaclass=PrintNameMeta):
    pass

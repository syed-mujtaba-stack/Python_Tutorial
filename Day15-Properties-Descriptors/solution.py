# Day 15 Solution: Properties & Descriptors

class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('Age must be positive')
        self._age = value

p = Person(20)
p.age = 25
print('Age:', p.age)

class UpperDescriptor:
    def __get__(self, instance, owner):
        return instance._val.upper()
    def __set__(self, instance, value):
        instance._val = value

class Demo:
    text = UpperDescriptor()
    def __init__(self, text):
        self._val = text

d = Demo('python')
print('Descriptor:', d.text)

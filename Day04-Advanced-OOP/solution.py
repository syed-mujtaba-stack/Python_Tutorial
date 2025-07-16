# Day 4 Solution: Advanced OOP
from abc import ABC, abstractmethod

class DescribeMixin:
    def describe(self):
        return f'I am a {self.__class__.__name__}'

class Base:
    pass

class MyClass(DescribeMixin, Base):
    pass

obj = MyClass()
print(obj.describe())

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print('Meow!')

cat = Cat()
cat.speak()

# Day 14 Solution: Data Classes & NamedTuples
from dataclasses import dataclass
from collections import namedtuple

@dataclass
class Book:
    title: str
    author: str
    year: int

b = Book('Python 101', 'Ali', 2022)
print(b)

City = namedtuple('City', ['name', 'population'])
c = City('Karachi', 20000000)
print(c)

# Day 14 Script: Data Classes & NamedTuples Demo
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    marks: List[int] = field(default_factory=list)

s = Student('Sara', [85, 90, 95])
print(s)

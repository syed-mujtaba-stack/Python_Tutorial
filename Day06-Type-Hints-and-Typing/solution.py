# Day 6 Solution: Type Hints & Typing
from typing import List, Dict, Union

def lengths(words: List[str]) -> Dict[str, int]:
    return {word: len(word) for word in words}

print(lengths(['python', 'typing']))

def square(x: Union[int, float]) -> float:
    return float(x * x)

print(square(3))
print(square(2.5))

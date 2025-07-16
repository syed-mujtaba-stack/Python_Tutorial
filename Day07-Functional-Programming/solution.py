# Day 7 Solution: Functional Programming
from functools import reduce

words = ['python', 'advanced', 'course']
uppercased = list(map(str.upper, words))
print('Uppercase:', uppercased)

nums = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2 == 1, nums))
print('Odd numbers:', odds)

factorial = reduce(lambda x, y: x * y, nums)
print('Factorial:', factorial)

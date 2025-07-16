# Day 22 Script: Advanced itertools & functools Demo
import itertools
from functools import reduce

nums = [1, 2, 3, 4, 5]
# itertools.accumulate
print('Accumulate:', list(itertools.accumulate(nums)))
# reduce
print('Product:', reduce(lambda x, y: x * y, nums))

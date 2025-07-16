# Day 22 Solution: Advanced itertools & functools
import itertools
from functools import partial

# 1. All pairs
pairs = list(itertools.combinations([1, 2, 3, 4], 2))
print('Pairs:', pairs)

# 2. Partial function
mul10 = partial(lambda x, y: x * y, 10)
print('10 * 5 =', mul10(5))

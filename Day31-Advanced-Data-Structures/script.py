# Day 31 Script: Advanced Data Structures Demo
from collections import deque, namedtuple

# Double-ended queue
d = deque('abc')
d.append('d')      # Add to right
d.appendleft('z')  # Add to left
print('Deque:', d)

# Named tuple
Point = namedtuple('Point', 'x y')
p = Point(10, 20)
print('Point:', p.x, p.y)

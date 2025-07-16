# Day 2 Solution: Generators & Iterators

def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i

for num in even_numbers(10):
    print(num)

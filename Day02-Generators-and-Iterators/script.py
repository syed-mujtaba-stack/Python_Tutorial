# Day 2 Script: Generators & Iterators Demo

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print('Fibonacci numbers below 20:')
for num in fibonacci(20):
    print(num)

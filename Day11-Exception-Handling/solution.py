# Day 11 Solution: Exception Handling

class NegativeValueError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeValueError('Negative value!')
    return n

try:
    check_positive(-5)
except NegativeValueError as e:
    print('Caught:', e)

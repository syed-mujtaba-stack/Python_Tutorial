# Day 17 Script: Testing Demo (pytest style)
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

print('pytest will discover and run test_add() if saved as test_*.py')

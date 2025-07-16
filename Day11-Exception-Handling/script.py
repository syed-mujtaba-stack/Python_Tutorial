# Day 11 Script: Exception Handling Demo

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Cannot divide by zero!')
        return None
    finally:
        print('Division attempted.')

safe_divide(10, 0)
safe_divide(10, 2)

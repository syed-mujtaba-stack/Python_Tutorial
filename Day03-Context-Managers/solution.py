# Day 3 Solution: Context Managers

class LogContext:
    def __enter__(self):
        print('Entering context...')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting context...')

with LogContext() as ctx:
    print('Inside the context block')

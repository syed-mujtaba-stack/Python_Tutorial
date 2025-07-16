# Day 3 Script: Context Managers Demo
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f'Acquiring resource: {name}')
    yield
    print(f'Releasing resource: {name}')

with managed_resource('Database Connection'):
    print('Working with the resource...')

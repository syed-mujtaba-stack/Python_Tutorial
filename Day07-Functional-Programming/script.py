# Day 7 Script: Functional Programming Demo
import itertools

def infinite_counter(start=0):
    for n in itertools.count(start):
        print(n)
        if n >= 3:
            break

infinite_counter()

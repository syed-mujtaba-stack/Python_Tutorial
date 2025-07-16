# Day 23 Solution: Advanced Logging & Debugging
import logging
import pdb

logging.basicConfig(level=logging.INFO)

def check_positive(n):
    pdb.set_trace()
    if n < 0:
        logging.error('Negative value!')
    else:
        logging.info('Value is positive')

check_positive(-3)

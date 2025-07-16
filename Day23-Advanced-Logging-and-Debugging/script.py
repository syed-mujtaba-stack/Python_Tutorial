# Day 23 Script: Advanced Logging & Debugging Demo
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

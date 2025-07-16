# Day 12 Solution: Regular Expressions
import re

text = 'Contact us at info@example.com or support@abc.org.'
pattern = r'[\w.-]+@[\w.-]+\.[a-zA-Z]+'
emails = re.findall(pattern, text)
print('Emails:', emails)

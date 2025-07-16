# Day 12 Script: Regular Expressions Demo
import re

text = 'My phone numbers are 123-456-7890 and (555) 555-5555.'
pattern = r'(\d{3})[- )]+(\d{3})[- ]?(\d{4})'
phones = re.findall(pattern, text)
print('Phone numbers:', phones)

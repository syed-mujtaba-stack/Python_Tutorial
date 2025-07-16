# Day 10 Solution: File Handling
import csv
import json

# 1. Save list of dicts to CSV
people = [
    {'name': 'Ali', 'age': 30},
    {'name': 'Sara', 'age': 25}
]
with open('people.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(people)

# 2. Load JSON file and print data
with open('people.json', 'w') as f:
    json.dump(people, f)

with open('people.json') as f:
    data = json.load(f)
    print(data)

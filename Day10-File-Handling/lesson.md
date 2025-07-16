# Day 10: Advanced File Handling (CSV, JSON, XML)

Python makes it easy to read and write various file formats, including CSV, JSON, and XML.

**CSV Example:**
```python
import csv
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Ali', 30])
```

**JSON Example:**
```python
import json
data = {'name': 'Sara', 'age': 25}
with open('data.json', 'w') as f:
    json.dump(data, f)
```

**XML Example:**
```python
import xml.etree.ElementTree as ET
root = ET.Element('person')
ET.SubElement(root, 'name').text = 'Zara'
tree = ET.ElementTree(root)
tree.write('data.xml')
```

---
**Pro Tip:**
Always use context managers (`with`) when working with files to ensure proper resource cleanup.

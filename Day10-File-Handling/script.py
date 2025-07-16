# Day 10 Script: File Handling Demo
import xml.etree.ElementTree as ET

root = ET.Element('books')
for i in range(2):
    book = ET.SubElement(root, 'book')
    ET.SubElement(book, 'title').text = f'Book {i+1}'
    ET.SubElement(book, 'author').text = f'Author {i+1}'
tree = ET.ElementTree(root)
tree.write('books.xml')

print('books.xml created!')

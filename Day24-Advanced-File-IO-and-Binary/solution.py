# Day 24 Solution: Advanced File I/O & Binary Data
import mmap

# Write bytes
data = b'\x01\x02\x03'
with open('mydata.bin', 'wb') as f:
    f.write(data)

# Read bytes
with open('mydata.bin', 'rb') as f:
    print('Read:', f.read())

# Memory map
with open('mydata.bin', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)
    print('mmap:', mm[:])
    mm.close()

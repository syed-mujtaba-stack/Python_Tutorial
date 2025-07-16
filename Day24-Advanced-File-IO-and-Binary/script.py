# Day 24 Script: Advanced File I/O & Binary Demo
import struct

# Pack data into binary format
packed = struct.pack('iif', 1, 2, 3.14)
with open('packed.bin', 'wb') as f:
    f.write(packed)

# Unpack data
with open('packed.bin', 'rb') as f:
    data = f.read()
    unpacked = struct.unpack('iif', data)
    print('Unpacked:', unpacked)

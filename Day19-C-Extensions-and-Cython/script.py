# Day 19 Script: C Extensions & Cython Demo
# Demo: Use ctypes to call a C function from a shared library (DLL/SO)
import ctypes
# Suppose you have compiled mymath.c to mymath.so or mymath.dll
# mymath.c: int add(int a, int b) { return a + b; }
# mymath.so (Linux/Mac) or mymath.dll (Windows)
# lib = ctypes.CDLL('./mymath.so')
# print(lib.add(2, 3))
print('See comments for ctypes/Cython usage.')

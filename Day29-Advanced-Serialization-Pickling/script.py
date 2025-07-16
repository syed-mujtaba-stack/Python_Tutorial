# Day 29 Script: Advanced Serialization & Pickling Demo
import pickle

class Demo:
    def __init__(self, value):
        self.value = value
obj = Demo(99)

with open('demo.pkl', 'wb') as f:
    pickle.dump(obj, f)

with open('demo.pkl', 'rb') as f:
    loaded = pickle.load(f)
    print('Demo value:', loaded.value)

# Day 29 Solution: Advanced Serialization & Pickling
import pickle

obj = {'x': 42, 'y': [1, 2, 3]}
with open('obj.pkl', 'wb') as f:
    pickle.dump(obj, f)

with open('obj.pkl', 'rb') as f:
    loaded = pickle.load(f)
    print('Loaded:', loaded)

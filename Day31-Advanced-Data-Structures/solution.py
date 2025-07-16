# Day 31 Solution: Advanced Data Structures
from collections import Counter, defaultdict

def word_freq(sentence):
    return Counter(sentence.split())

def group_words(words):
    d = defaultdict(list)
    for word in words:
        d[word[0].lower()].append(word)
    return d

s = 'Python is awesome and Python is fun'
print('Word frequencies:', word_freq(s))
print('Grouped words:', dict(group_words(s.split())))

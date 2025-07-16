# Day 20 Solution: Mini Project
import requests
import matplotlib.pyplot as plt

# Example: Plot lengths of post titles from jsonplaceholder
url = 'https://jsonplaceholder.typicode.com/posts'
resp = requests.get(url)
data = resp.json()
title_lengths = [len(post['title']) for post in data]
plt.plot(title_lengths)
plt.title('Title Lengths of Posts')
plt.xlabel('Post #')
plt.ylabel('Title Length')
plt.show()

# Day 20 Script: Mini Project Demo
import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
print('Title of page:', soup.title.string)

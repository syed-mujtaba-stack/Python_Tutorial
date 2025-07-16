# Day 28 Script: Advanced Unittesting & Mocking Demo
from unittest.mock import patch
import requests

def get_title(url):
    return requests.get(url).json().get('title')

with patch('requests.get') as mock_get:
    mock_get.return_value.json.return_value = {'title': 'Mocked!'}
    print(get_title('http://example.com'))

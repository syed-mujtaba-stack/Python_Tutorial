# Day 28 Solution: Advanced Unittesting & Mocking
import unittest
from unittest.mock import patch
import requests

def fetch_json(url):
    return requests.get(url).json()

class TestFetchJson(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_json(self, mock_get):
        mock_get.return_value.json.return_value = {'result': 123}
        data = fetch_json('http://example.com')
        self.assertEqual(data['result'], 123)

if __name__ == '__main__':
    unittest.main()

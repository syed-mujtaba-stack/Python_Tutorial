# Day 40 Solution: Advanced Testing Strategies
import pytest

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Tests
def test_palindrome():
    # Basic cases
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    
    # Edge cases
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("A") == True  # Single uppercase
    assert is_palindrome("!@#") == True  # No alphanumeric chars
    assert is_palindrome("A man, a plan, a canal: Panama!") == True  # With punctuation

# To run tests: python -m pytest solution.py -v

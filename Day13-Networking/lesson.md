# Day 13: Networking in Python

Python offers built-in modules for networking, such as `socket` for low-level TCP/UDP and `requests` for HTTP.

**Socket Example:**
```python
import socket
s = socket.socket()
s.connect(('example.com', 80))
s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
print(s.recv(1024))
s.close()
```

**Requests Example:**
```python
import requests
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
```

---
**Pro Tip:**
Use `requests` for HTTP APIs and `socket` for custom protocols or lower-level access.

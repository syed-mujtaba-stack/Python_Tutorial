# Day 38: Network Programming

Learn to create networked applications using Python's built-in modules.

**Socket Programming:**
```python
import socket

# TCP Server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65432))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```

**HTTP Client with requests:**
```python
import requests

response = requests.get('https://api.github.com')
print(response.json())
```

---
**Pro Tip:**
Use higher-level libraries like `requests` for HTTP and `websockets` for WebSockets instead of raw sockets when possible.

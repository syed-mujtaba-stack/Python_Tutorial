# Day 13 Script: Networking Demo
import socket

host = 'example.com'
port = 80
s = socket.socket()
s.connect((host, port))
s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
print(s.recv(1024))
s.close()

# Day 38 Solution: Network Programming
import socket
import threading

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 9999))
        s.listen()
        print("Server listening on port 9999...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(b'Echo: ' + data)

def client_send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 9999))
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received:', data.decode())

# Start server in a separate thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Give server time to start
import time
time.sleep(1)

# Test the client
client_send_message("Hello, Network!")
# Note: In a real application, you'd run server and client separately

# Day 38 Script: Network Programming Demo
import http.server
import socketserver
import threading
import requests

# Simple HTTP Server
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello from Python HTTP Server!')

def run_http_server():
    PORT = 8000
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

# Start HTTP server in a separate thread
http_thread = threading.Thread(target=run_http_server, daemon=True)
http_thread.start()

# HTTP Client Example
def fetch_url(url):
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
    except Exception as e:
        print(f"Error: {e}")

# Test HTTP client
print("\nTesting HTTP Client:")
fetch_url('http://localhost:8000')

# Note: In a real application, you'd run the server and client separately

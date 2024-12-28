import http.server
import socketserver
import os

# Port to host the HTTP server
PORT = 8080

# File to be downloaded
FILE_NAME = "example.txt"

# Create the file to be shared
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        f.write("This is a test file. Have fun learning!")

# Define the HTTP server handler
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/download':
            self.path = f'/{FILE_NAME}'
        return super().do_GET()

# Set up the HTTP server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving on port {PORT}. Share this link: http://<your-ip>:{PORT}/download")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()

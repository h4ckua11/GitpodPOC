from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        # Preflight request response (needed for CORS)
        self.send_response(200)
        self.send_headers()
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        print("Received:", post_data)

        self.send_response(200)
        self.send_headers()
        self.end_headers()
        self.wfile.write(b"Received")

    def send_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")  # Allow all origins
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

server_address = ("0.0.0.0", 8080)
httpd = HTTPServer(server_address, SimpleHandler)
print("Listening for incomming connections...")
httpd.serve_forever()

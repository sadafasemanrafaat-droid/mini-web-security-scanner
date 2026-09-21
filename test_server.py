from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        body = b"Hello from test server"

        self.send_response(200)
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        self.wfile.write(body)


server = HTTPServer(("127.0.0.1", 8001), Handler)

print("Test server running on port 8001")

server.serve_forever()
#!/usr/bin/python3
"""Simple RESTful API using Python's http.server module"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Server(BaseHTTPRequestHandler):
    # Helper methods
    def _send_text(self, code, text, charset="utf-8"):
        body = text.encode(charset)
        self.send_response(code)
        self.send_header("Content-Type", f"text/plain; charset={charset}")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(body)

    def _send_json(self, code, obj):
        body = json.dumps(obj, separators=(",", ":")).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(body)

    def do_HEAD(self):
        if self.path == "/":
            self._send_text(200, "")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/status":
            self._send_text(200, "")
        elif self.path == "/info":
            self._send_json(200, {"version": "1.0", "description": "A simple API built with http.server"})
        else:
            # For HEAD requests to undefined paths, still send 404 but an empty body as per HEAD request nature
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Allow", "GET,POST,HEAD,OPTIONS")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(200, data)
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send_json(200, info)
        else:
             self._send_json(404, {"error": "Not Found"})

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data.decode("utf-8"))
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"received": data}
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"error": "Invalid JSON"}
        self.wfile.write(json.dumps(response, separators=(",", ":")).encode("utf-8"))

def run(server_class=HTTPServer, handler_class=Server):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        print(f"Starting server on port {server_address[1]}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server")
        httpd.server_close()

if __name__ == "__main__":
    run()
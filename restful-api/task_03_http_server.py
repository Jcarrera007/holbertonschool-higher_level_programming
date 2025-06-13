#!/usr/bin/python3
"""Simple RESTful API using Python's http.server module"""

from http.server
import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="application/json"):
        self.send_response(status_code)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self._set_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data, separators=(",", ":"))
            self.wfile.write(response.encode("utf-8"))

        elif self.path == "/status":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self._set_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            response = json.dumps(info, separators=(",", ":"))
            self.wfile.write(response.encode("utf-8"))

        else:
            self._set_headers(404)
            error = {"error": "Not found"}
            response = json.dumps(error, separators=(",", ":"))
            self.wfile.write(response.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode("utf-8"))
            self._set_headers(200)
            response = {"received": data}
        except json.JSONDecodeError:
            self._set_headers(400)
            response = {"error": "Invalid JSON"}

        self.wfile.write(json.dumps(response, separators=(",", ":")).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()

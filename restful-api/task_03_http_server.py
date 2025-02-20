#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

"""
Holberton School - Python API Exercise

This script uses the requests library to fetch posts from the JSONPlaceholder API.
It prints the titles of all posts and also saves them into a CSV file.
"""
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Got GET request %s" % (self.path))

        if self.path == '/':
            self.send_response(200)


  
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(
              b"Page not found."
            )


def run():

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()


run()

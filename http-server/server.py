#!/usr/bin/python3
import http.server, socketserver, os
import _thread as thread
import logging, cgi, base64
from urllib.parse import urlparse


PORT = 8000
DIR = '/work/dir/path'
ADDRESS = '127.0.0.1'
USERNAME = "username"
PASSWORD = "password"
SECURE_URL = "/auth.html"


class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self._auth = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
        super().__init__(*args)

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Authorization"')
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        logging.error(self.headers)
        if urlparse(self.path).path == SECURE_URL:
            if self.headers.get("Authorization") is None:
                self.do_AUTHHEAD()
            elif self.headers.get("Authorization") == "Basic " + self._auth:
                http.server.SimpleHTTPRequestHandler.do_GET(self)
            else:
                self.do_AUTHHEAD()
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path.startswith('/kill_server'):

            def kill_me_please(server):
                server.shutdown()
            thread.start_new_thread(kill_me_please, (httpd,))
            self.send_error(500)
        else:
            logging.error(self.headers)
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
                                    environ={'REQUEST_METHOD': 'POST',
                                             'CONTENT_TYPE': self.headers['Content-Type']})
            for item in form.list:
                logging.error(item)
            http.server.SimpleHTTPRequestHandler.do_GET(self)


class MyHTTPServer(socketserver.TCPServer):

    def server_bind(self):
        import socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)


os.chdir(DIR)
server_address = (ADDRESS, PORT)
httpd = MyHTTPServer(server_address, Handler)

try:
    httpd.serve_forever()
finally:
    httpd.server_close()

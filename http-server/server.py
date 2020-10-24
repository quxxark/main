#!/usr/bin/python3.8
import http.server, socketserver, os
import _thread as thread


PORT = 8000
DIR = ''  # Directory with the local html-pages
ADDRESS = '127.0.0.1'


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        if self.path.startswith('/kill_server'):

            def kill_me_please(server):
                server.shutdown()
            thread.start_new_thread(kill_me_please, (httpd,))
            self.send_error(500)


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

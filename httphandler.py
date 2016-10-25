# encoding: utf-8

from BaseHTTPServer import BaseHTTPRequestHandler
from SocketServer import BaseRequestHandler
from request import request

class httpHandler(BaseHTTPRequestHandler):

    def __init__(self, processor, request, client_address, server):
        self.processor = processor

        BaseRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        if self.processor:
            res = self.processor.onProcessRequest(request(self.path, 'GET'))
            if res is None:
                self.protocal_version = "HTTP / 1.1"
                self.send_response(400)
            else:
                self.protocal_version = "HTTP / 1.1"
                self.send_response(res.code)
                self.end_headers()
                self.wfile.write(res.buff)
        else:
            self.protocal_version = "HTTP / 1.1"
            self.send_response(400)

    def do_POST(self):
        # todo

        pass
# encoding: utf-8

from webserver import webServer

server = webServer()

@server.route('/{name}')
def index(name=None):
    if name:
        return '<html><body><h3>hello %s</h3></body></html>' % (name)
    else:
        return '<html><body><h3>hello world</h3></body></html>'

server.start_forever('127.0.0.1', 9999)
# encoding: utf-8

from BaseHTTPServer import HTTPServer
from functools import partial
from httphandler import httpHandler
import re
from response import response

class webServer(object):
    def __init__(self):
        self.mapOperation = {}
        self.handler = partial(httpHandler, self)
        pass

    def start_forever(self, ip, port):
        server = HTTPServer((ip, port), self.handler)
        server.serve_forever()

    def route(self, path, methods=['GET']):
        def fun(f):
            regPath = self.__buildPath(path)
            for operation in methods:
                if not self.mapOperation.has_key(operation):
                    self.mapOperation[operation] = {}
                self.mapOperation[operation][regPath] = f

            return f

        return fun

    def __buildPath(self, path):
        def named_groups(matchobj):
            return '(?P<{0}>[a-zA-Z0-9_-]+)[/]?'.format(matchobj.group(1))

        re_str = re.sub(r'{([a-zA-Z0-9_-]+)}[/]?', named_groups, path)
        re_str = ''.join(('^', re_str, '$',))
        return re.compile(re_str)

    def __matchPath(self, pathReg, path):
        params = pathReg.match(path)
        try:
            return params.groupdict()
        except AttributeError:
            return None

    def onProcessRequest(self, request):
        ret = None

        if self.mapOperation.has_key(request.method):
            for pathReg, handle in self.mapOperation[request.method].items():
                params = self.__matchPath(pathReg, request.path)
                if params:
                    ret = handle(**params)
                    if not isinstance(ret, response):
                        ret = response(200, str(ret))

        return ret
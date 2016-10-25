# encoding: utf-8

class request:
    def __init__(self, path, method):
        self.path = path
        self.method = method

    def getPath(self):
        return self.path

    def getMethod(self):
        return self.method
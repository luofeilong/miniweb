# encoding: utf-8

class response:
    def __init__(self, code, buff):
        self.code = code
        self.buff = buff
        self.protocalVersion = "HTTP / 1.1"
        pass

    def setCode(self, code):
        self.code = code

    def setBuff(self, buff):
        self.buff = buff
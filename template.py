import re

class coder(object):
    def __init__(self):
        self.codelines = []
        self.level = 0
        self.tabspace = 4

    def addLine(self, line):
        self.codelines.append(''.join([' '*self.level*self.tabspace, line, '\n']))

    def enterSection(self):
        self.level += 1

    def exitSection(self):
        self.level -= 1

    def __str__(self):
        return ''.join(self.codelines)

class Template(object):
    def __init__(self, templateStr, **context):
        self.coder = coder()

        params = [key for key in context.keys()]

        self.coder.addLine('def myrender(%s):'%','.join(params))
        self.coder.enterSection()
        self.coder.addLine('listStr=[]')
        tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", templateStr)
        print tokens
        for token in tokens:
            token = token.strip()
            if token[:2] == '{#':
                continue
            elif token[:2] == '{%':
                tmp = token[2:-2].strip()
                columns = tmp.split()
                if len(columns) > 0:
                    if columns[0] == 'if':
                        self.coder.addLine("%s:"%tmp)
                        self.coder.enterSection()
                    elif columns[0] == 'for':
                        self.coder.addLine("%s:"%tmp)
                        self.coder.enterSection()
                    elif columns[0].startswith('end'):
                        self.coder.exitSection()
                continue
            elif token[:2] == '{{':
                self.coder.addLine("listStr.append(str(%s))"%token[2:-2].strip())
                continue
            else:
                token = token.replace('\n', ' ')
                self.coder.addLine("listStr.append('%s')"%token)
        self.coder.addLine(r"return ''.join(listStr)")

        global_namespace = {}
        exec (str(self.coder), global_namespace)
        myfunc = global_namespace['myrender']
        self.renderStr = myfunc(**context)

    def __str__(self):
        return self.renderStr
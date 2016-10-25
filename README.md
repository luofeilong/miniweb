# miniweb

这是一个简单的web框架的练手尝试，不适合正式使用

可以直接运行pyton webserver_test.py进行测试，运行后，通过浏览器打开http://localhost:9999/world进行查看。

使用demo代码

```python
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
```
'''
第一个web项目 Hello Tornado
'''

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

# 设置默认参数
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# 定义视图处理函数
class IndexHandler(RequestHandler):
    # 重写get处理方式
    def get(self):
        # 读取客户端的名字
        name = self.get_argument('yourname', 'Guest')
        # 向客户端发送一个数据
        self.write("<h1>Hello, " + name + "</h1>"
                   + "(Try to type your name in the url by adding:/?yourname=Bob)"
                   + "<br/>It is the main page."
                   + "<br/>(Go to another page:/1)"
                   )

class Page1Handler(RequestHandler):
    # 重写get处理方式
    def get(self):
        self.write("This is Page 1.")

# 程序入口
if __name__ == '__main__':
    app = Application([
        # 定义路由访问
        (r'/',IndexHandler),
        (r'/1',Page1Handler)
    ])
    # 监听端口
    app.listen(options.port)
    # 启用tornado内置的服务器轮询监听
    IOLoop.current().start()
'''
第三个web项目 动态页面
'''

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import os

# 设置默认参数
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# 定义视图处理函数
class IndexHandler(RequestHandler):
    # 重写get处理方式
    def get(self):
        self.render('index.html')


# 显示文件名（包含子文件夹中所有文件）
class NameHandler(RequestHandler):

    # 重写post处理方式
    def post(self):
        # 获取访客名字
        newname = self.get_argument('name')
        # 读取过去访客列表
        template_path = self.get_template_path()
        filename = 'a.txt'
        visitor_list = []
        f = open(os.path.join(template_path, filename), 'r')
        if not f:
            self.write('Error.')
            return
        contents = f.readlines()
        for name in contents:
            name = name.strip('\n')
            visitor_list.append(name)
        # 将新访客写入列表
        visitor_list.append(newname)
        # 将列表写入文件
        with open(os.path.join(template_path, filename), 'w') as up:
            for name in visitor_list:
                up.write(name)
                up.write('\n')
        # 显示结果
        self.render('listname.html', namelist=visitor_list)

# 程序入口
if __name__=='__main__':
    app = Application(
        # 定义路由访问
        handlers=[(r'/', IndexHandler),
                  (r'/name', NameHandler)
                  ],
        template_path=os.path.join(os.path.dirname(__file__), "temp3")
    )
    # 监听端口
    app.listen(options.port)
    # 启用tornado内置的服务器轮询监听
    IOLoop.current().start()
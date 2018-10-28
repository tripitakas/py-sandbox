'''
第二个web项目 页面中相应遍历文件或文件夹，读取文件内容并显示在页面
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
class ListAllHandler(RequestHandler):

    # 重写post处理方式
    def post(self):
        template_path = self.get_template_path()
        template_list = getallfiles(template_path)
        self.render('listdir.html', dir=template_path, dirlist=template_list )
def getallfiles(path):
    allfile=[]
    for dirpath,dirnames,filenames in os.walk(path):
        for dir in dirnames:
            allfile.append(os.path.join(dirpath,dir))
        for name in filenames:
            allfile.append(os.path.join(dirpath, name))
    return allfile
# 用户想保存数据
class ToSaveHandler(RequestHandler):
    # 重写post处理方式
    def post(self):
        self.render('savedata.html')

# 保存用户数据
class SaveHandler(RequestHandler):
    # 重写post处理方式
    def post(self):
        source_text = self.get_argument('source')
        filename = self.get_argument('filename')
        template_path = self.get_template_path()
        with open(os.path.join(template_path, filename), 'w') as up:
            up.write(source_text)
        self.write('Finished.')
        self.render('index.html')

# 打开文件
class OpenHandler(RequestHandler):
    # 重写post处理方式
    def post(self):
        filename = self.get_argument('fn')
        try:
            with open(filename, 'r') as f:
                content = f.read()
            self.render('showfile.html', filename=filename, content=content)
        except:
                template_list = getallfiles(filename)
                self.render('listdir.html', dir=filename, dirlist=template_list)



# 程序入口
if __name__=='__main__':
    app = Application(
        # 定义路由访问
        handlers=[(r'/', IndexHandler),
                  (r'/listall', ListAllHandler),
                  (r'/save', ToSaveHandler),
                  (r'/savetofile', SaveHandler),
                  (r'/openfile', OpenHandler)
                  ],
        template_path=os.path.join(os.path.dirname(__file__), "temp")
    )
    # 监听端口
    app.listen(options.port)
    # 启用tornado内置的服务器轮询监听
    IOLoop.current().start()
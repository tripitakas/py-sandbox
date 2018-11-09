# -*- coding: utf-8 -*-  unicode 8 编码

from tornado.ioloop import IOLoop 
from tornado.web import Application, RequestHandler
from os import path, listdir

BASE_DIR = path.dirname(__file__)


class MainHandler(RequestHandler):
    def get(self):
    #    self.write('<ol>Hello world</ol>')
        self.write('<a href="url">Link text</a>')


class SecHandler(RequestHandler):
    def get(self, name):
      #  self.write('<ol>Hello worldooo</ol>')
        self.render('test.html')


if __name__ == '__main__':
    handlers = [MainHandler, SecHandler]
    app = Application([(r'/', MainHandler), [r'/(\w+)', SecHandler]],
    debug=True, template_path=path.join(BASE_DIR, 'views'))
    app.listen(8003)
    print('Start http://localhost:8003')
    IOLoop.current().start()
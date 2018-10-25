from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from os import path, listdir
from file_util import load_json

class MainHandler(RequestHandler):
    def get(self):
        names = sorted([f[:-4] for f in listdir('cut-result') if f.endswith('.txt')])
# 失败了 完全看不懂 毫无tornado的基础
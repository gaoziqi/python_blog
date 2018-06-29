import tornado.ioloop
import tornado.web
import psycopg2
from tornado.options import parse_command_line

class GetHandler(tornado.web.RequestHandler):

    def get(self):
        key = self.get_argument('key')
        self.application.cu.execute(f'SELECT v FROM teststr WHERE k = {key}')
        res = self.application.cu.fetchone()
        self.write(str(res[0]) if res else '不存在')


class SetHandler(tornado.web.RequestHandler):

    def post(self):
        key = self.get_argument('key')
        value = self.get_argument('value')
        self.application.cu.execute(f'SELECT v FROM teststr WHERE k = {key}')
        res = self.application.cu.fetchone()
        if res:
            self.application.cu.execute(f"UPDATE teststr SET v = '{value}' WHERE k = {key}")
        else:
            self.application.cu.execute(f"INSERT INTO teststr VALUES ({key}, '{value}')")
        self.application.conn.commit()
        self.write('完成')

class CodeHandler(tornado.web.RequestHandler):

    def get(self):
        filename = 'server.py'
        self.set_header("Content-Type", 'application/octet-stream')
        self.set_header("Content-Disposition", "%s%s" % ("attachment; filename=", filename))
        buffer_size = 4096
        with open('/code/%s' % filename, 'rb') as r:
            while True:
                data = r.read(buffer_size)
                if not data:
                    break
                self.write(data)
        self.finish()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('HELLO WORLD')


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/get', GetHandler),
            (r'/set', SetHandler),
            (r'/code', CodeHandler),
            (r'/', MainHandler)
        ]
        settings = {} #'static_path', 'static_url_prefix'
        self.conn = psycopg2.connect(database='postgres', user='postgres', password='postgres', host='db', port='5432')
        self.cu = self.conn.cursor()
        self.cu.execute("CREATE TABLE IF NOT EXISTS teststr(k INT PRIMARY KEY, v text);")
        self.conn.commit()
        tornado.web.Application.__init__(self, handlers, debug = True, **settings)


if __name__ == '__main__':
    parse_command_line()
    app = Application()
    app.listen(13017)
    tornado.ioloop.IOLoop.instance().start()

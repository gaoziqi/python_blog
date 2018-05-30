import tornado.ioloop
import tornado.web
import psycopg2

class GetHandler(tornado.web.RequestHandler):

    def get(self):
        key = self.get_argument('key')
        self.application.cu.execute(f'SELECT v FROM test WHERE k = {key}')
        res = self.application.cu.fetchone()
        self.write(res[0] if res else '不存在')


class SetHandler(tornado.web.RequestHandler):

    def get(self):
        key = self.get_argument('key')
        value = self.get_argument('value')
        self.application.cu.execute(f'SELECT v FROM test WHERE k = {key}')
        res = self.application.cu.fetchone()
        if res:
            self.application.cu.execute(f'UPDATE test SET v = {value} WHERE k = {key}')
        else:
            self.application.cu.execute(f'INSERT INTO test VALUES ({key}, {value})')
        self.application.conn.commit()
        self.write('完成')


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('HELLO WORLD')


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/get', GetHandler),
            (r'/set', SetHandler),
            (r'/', MainHandler)
        ]
        settings = {} #'static_path', 'static_url_prefix'
        self.conn = psycopg2.connect(database='postgres', user='postgres', password='postgres', host='db', port='5432')
        self.cu = self.conn.cursor()
        self.cu.execute("DROP TABLE IF EXISTS test;CREATE TABLE test(k INT PRIMARY KEY, v INT);")
        self.conn.commit()
        tornado.web.Application.__init__(self, handlers, debug = True, **settings)


if __name__ == '__main__':
    app = Application()
    app.listen(13017)
    tornado.ioloop.IOLoop.instance().start()

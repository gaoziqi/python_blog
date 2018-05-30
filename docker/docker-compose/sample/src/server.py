import tornado.ioloop
import tornado.web
import psycopg2

class GetHandler(tornado.web.RequestHandler):

    def get(self):
        key = self.get_argument('key')
        self.cu.execute(f'SELECT v FROM test WHERE k = {key}')
        res = self.cu.fetchone()
        self.write(res[0] if res else '不存在')
        self.finish()

class SetHandler(tornado.web.RequestHandler):

    def get(self):
        key = self.get_argument('key')
        value = self.get_argument('value')
        self.cu.execute(f'SELECT v FROM test WHERE k = {key}')
        res = self.cu.fetchone()
        if res:
            self.cu.execute(f'UPDATE test SET v = {value} WHERE k = {key}')
        else:
            self.cu.execute(f'INSERT INTO test VALUES ({key}, {value})')
        self.conn.commit()
        self.write('完成')
        self.finish()

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'get', GetHandler),
            (r'set', SetHandler)
        ]
        settings = {} #'static_path', 'static_url_prefix'
        self.conn = psycopg2.connect(database='postgres', user='postgres', password='postgres', host='0.0.0.0', port='5432')
        self.cu = self.conn.cursor()
        self.cu.execute("CREATE TABLE test(k INT PRIMARY KEY, v INT)")
        self.conn.commit()
        tornado.web.Application.__init__(self, handlers, debug = True, **settings)


if __name__ == '__main__':
    app.listen(13017)
    tornado.ioloop.IOLoop.instance().start()

import tornado.ioloop
import tornado.web
import tornado.options
from setting import settings

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(r'template/index.html')

application= tornado.web.Application([
    (r'/',HomeHandler),

],**settings)

if __name__ == "__main__":
    port = 8888
    print(f'🌀 Tornado is listening on port {port}')
    tornado.options.define("port", default=port, help="Run server on a specific port", type=int)
    tornado.options.parse_command_line()
    application_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    application_server.listen(tornado.options.options.port)
    application_server.start()
    tornado.ioloop.IOLoop.instance().start()
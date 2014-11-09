import tornado.web
import logging

logger = logging.getLogger(__name__)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        self.finish()

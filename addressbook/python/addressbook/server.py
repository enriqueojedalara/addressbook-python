#!/usr/bin/python2.7
"""A single-threaded HTTP server.

"""
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from addressbook.handlers.main import (
	UserHandler,
    BookHandler,
    TwitterHandler,
    NotFoundErrorHandler,
)
from addressbook.utils.conf import settings


logger = logging.getLogger(__name__)


class Server():
	def start(self):
		application = tornado.web.Application([
			(r"/api/login", UserHandler),
			(r"/api/contacts", BookHandler),
			(r"/api/tweets/(.*)", TwitterHandler),
			(r"/(.*)", tornado.web.StaticFileHandler, {"path": settings.front_end_path}),
		])

		ssl_options = {
			'certfile': settings.ssl_crt,
			'keyfile': settings.ssl_key,
		}
		server = tornado.httpserver.HTTPServer(application, ssl_options=ssl_options)
		server.listen(settings.port)
		logger.info('Server started on port %d' % settings.port)
		tornado.ioloop.IOLoop.instance().start()




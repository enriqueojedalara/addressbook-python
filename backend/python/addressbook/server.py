#!/usr/bin/python2.7

"""A single-threaded HTTP server.

This script is used to start the HTTP server
"""

import tornado.httpserver
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Server structure completed!")
		self.finish()

application = tornado.web.Application([
	(r"/", MainHandler)
])

if __name__ == "__main__":
	ssl_options = {
		'certfile': '../../conf/server.crt',
		'keyfile': '../../conf/server.key',
	}
	server = tornado.httpserver.HTTPServer(application, ssl_options=ssl_options)
	server.listen(8008)
	tornado.ioloop.IOLoop.instance().start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'mjhans'

from  tornado.ioloop import IOLoop
from tornado import gen
from tornado.httpserver import HTTPServer
from restApplication import create_restful_app

##############################################################################
class http_server(object):

	#=========================================================================
	PORT = 8888
	PROCESS_NUM = 0 # all process
	HANDLERS = list()
	ISWSGI = False

	#=========================================================================
	def __init__(self, port=8888, process_num=0, handlers=[], wsgi=False):
		self.PORT = port
		self.PROCESS_NUM = process_num
		self.HANDLERS = handlers
		self.ISWSGI = wsgi

	#=========================================================================
	def start(self):
		try:

			app = create_restful_app(self.ISWSGI, self.HANDLERS)
			server = HTTPServer(app)
			server.bind(self.PORT)
			server.start(self.PROCESS_NUM)

			print "PORT : %s, Process : %s" % (self.PORT, self.PROCESS_NUM)
			IOLoop.current().start()

		except Exception, msg:
			print "[tornado server start Exceptions : %s]" % msg

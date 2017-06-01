#!/usr/bin/env python
#coding=utf8

__author__ = 'mjhans'

from  tornado.ioloop import IOLoop
from tornado import gen
from tornado.httpserver import HTTPServer

from Application import ftApplication

##############################################################################
class http_server(object):

	#=========================================================================
	PORT = 8888
	PROCESS_NUM = 0 # all process

	#=========================================================================
	def __init__(self, port=8888, process_num=0, handlers=[]):
		self.PORT = port
		self.PROCESS_NUM = process_num
		self.HANDLERS = handlers

	#=========================================================================
	def start(self):
		try:
			app = ftApplication(self.HANDLERS)
			server = HTTPServer(app)
			server.bind(self.PORT)
			server.start(self.PROCESS_NUM)
			IOLoop.clear_current().start()
		except Exception, msg:
			print "[tornado server start Exceptions : %s]" % msg





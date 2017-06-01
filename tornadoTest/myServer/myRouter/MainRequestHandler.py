#!/usr/bin/env python
#coding=utf8
__author__ = 'mjhans'


from tornadoServer.BaseHandler import BaseRequestHandler

##############################################################################
class MainRequestHandler(BaseRequestHandler):

	URI = "/api/ftids/main"
	#=========================================================================
	def get(self, *args, **kwargs):
		try:
			pass
		except Exception, msg:
			print msg
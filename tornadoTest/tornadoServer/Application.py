#!/usr/bin/env python
#coding=utf8

__author__ = 'mjhans'

from tornado.web import Application

class ftApplication(Application):

	#=========================================================================
	def __init__(self, handler_set_list=[]):

		handlers = []
		for handlers_set in handler_set_list:
			uri = r"/%s" % handlers_set[0]
			hd = handlers_set[1]
			handlers.append((uri, hd))

		Application.__init__(self, handlers)


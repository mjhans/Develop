#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mjhans'

from restfulMediatype import *
from define import *
from tornadoServer.ftRestfulException.RestfulAPIException import RestfulException
from tornado.web import RequestHandler, HTTPError
from json import dumps, loads

#=========================================================================
def get(*params, **kwargs):
	pass

#=========================================================================
def post(*params, **kwargs):
	pass

#=========================================================================
def put(*params, **kwargs):
	pass

#=========================================================================
def delete(*params, **kwargs):
	pass



def _exe(cls, method, *params, **kwargs):
		print "Method : %s" % method
		print "func : %s" % cls.func
		print "params: %s, %s" % (params, kwargs)

##############################################################################
class BaseRequestHandler(RequestHandler):

	#=========================================================================
	@classmethod
	def get(cls, *params, **kwargs):
		""" Executes get method """
		_exe('GET', *params, **kwargs)

	#=========================================================================
	def post(self, *params, **kwargs):
		""" Executes post method """
		self._exe('POST', *params, **kwargs)

	#=========================================================================
	def put(self, *params, **kwargs):
		""" Executes put method"""
		self._exe('PUT', *params, **kwargs)

	#=========================================================================
	def delete(self, *params, **kwargs):
		""" Executes put method"""
		self._exe('DELETE', *params, **kwargs)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mjhans'

"""
	토네이도의 Request Handler를 상속받은 클래스

	사용방법
		1. BaseRequestHandler 클래스를 상속받아 서브 클래스를 작성
		2. get, post, put, delete, patch 의 함수를 오버라이딩 하여 구현
		3.


"""

from tornado.web import RequestHandler
from json import dumps, loads
from datetime import datetime


##############################################################################
class BaseRequestHandler(RequestHandler):

	URI = "/"
	#=========================================================================
	def __init__(self, application=None, request=None, **kwargs):
		RequestHandler.__init__(self, application, request, **kwargs)

	#=========================================================================
	def prepare(self):
		# Request handler where requests and responses speak JSON.
		# Incorporate request JSON into arguments dictionary.
		if self.request.body:
			try:
				json_data = loads(self.request.body)
				self.request.arguments.update(json_data)
			except ValueError:
				message = 'Unable to parse JSON.'
				self.send_error(400, message=message) # Bad Request

		# Set up response dictionary.
		self.response = dict()

	#=========================================================================
	def set_default_headers(self):
		self.set_header('Content-Type', 'application/json')

	#=========================================================================
	def write_error(self, status_code, **kwargs):
		if 'message' not in kwargs:
			if status_code == 405:
				kwargs['message'] = 'Invalid HTTP method.'
			else:
				kwargs['message'] = 'Unknown error.'
		self.response = kwargs
		self.write_json()

	#=========================================================================
	def write_json(self):
		output = dumps(self.response)
		self.write(output)

	#=========================================================================
	@staticmethod
	def set_uri(uri):
		BaseRequestHandler.URI = uri

	#=========================================================================
	@staticmethod
	def get_uri():
		return BaseRequestHandler.URI

	#=========================================================================
	def __create_handler_info(self):
		cls_name = type(self).__name__
		return (self.URI, cls_name,)

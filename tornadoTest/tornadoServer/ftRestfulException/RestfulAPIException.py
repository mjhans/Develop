#!/usr/bin/env python
#coding=utf8

"""
	작성자 : 문중현
	내용:
		Restful API Exception class 정의

"""

__author__ = 'mjhans'


##############################################################################
class RestfulException(Exception):
	""" ftRestfulException class """

	#=========================================================================
	def __init__(self, message):
		Exception.__init__(message)
		self.message = message

	#=========================================================================
	def __str__(self):
		return repr(self.message)

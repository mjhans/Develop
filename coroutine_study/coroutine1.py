#!/usr/bin/env python
#coding=utf8

#=====================================================================================
def coroutine(func):
	def start(*args, **kwargs):
		cr = func(*args, **kwargs)
		cr.next()
		return cr
	return start

from collections import namedtuple
Result = namedtuple('Result', 'count average')

def averager():
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield average
		total += term
		count += 1
		average = total / count
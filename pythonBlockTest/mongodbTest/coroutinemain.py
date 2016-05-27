#!/usr/bin/env python
#coding=utf8

import os
from threading import Thread
from  mongo import *

THREAD_MAX_CNT = 10
#=====================================================================================
def coroutine(func):
	def start(*args, **kwargs):
		cr = func(*args, **kwargs)
		cr.next()
		return cr
	return start

#=====================================================================================
@coroutine
def startMongo():
	try:
		while True:
			conn = yield
			mongoUpdate(conn)
	except Exception, msg:
		raise Exception(msg)

##########################################################################################
if __name__ == "__main__":
	tlist = list()
	try:
		conn = mongodbconn()

		iter = startMongo()

		iter.send(conn)
		iter.send(conn)
		iter.send(conn)
		iter.send(conn)
		iter.send(conn)

		iter.send(conn)
		iter.send(conn)
		iter.send(conn)
		iter.send(conn)
		iter.send(conn)

	except Exception, msg:
		print msg

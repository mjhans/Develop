#!/usr/bin/env python
#coding=utf8

import os
from threading import Thread
from  mongo import *

THREAD_MAX_CNT = 10

def startMongo(conn):
	try:
		mongoUpdate(conn)
	except Exception, msg:
		raise Exception(msg)

##########################################################################################
if __name__ == "__main__":
	tlist = list()
	try:
		conn = mongodbconn()

		for i in range(THREAD_MAX_CNT):
			startMongo(conn)
		# startMongo(conn)
		# startMongo(conn)
		# startMongo(conn)
		# startMongo(conn)
		#
		# startMongo(conn)
		# startMongo(conn)
		# startMongo(conn)
		# startMongo(conn)
		# startMongo(conn)

	except Exception, msg:
		print msg

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
			t = Thread(target=startMongo, args=(conn,))
			tlist.append(t)
			t.start()

		for i in range(THREAD_MAX_CNT):
			tlist[i].join()

	except Exception, msg:
		print msg

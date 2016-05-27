#!/usr/bin/env python
#coding=utf8

import os
from multiprocessing import Process
from mongo import *

THREAD_MAX_CNT = 10

def startMongo():
	try:
		mongoUpdate(mongodbconn())
	except Exception, msg:
		raise Exception(msg)

##########################################################################################
if __name__ == "__main__":
	tlist = list()
	try:
		for i in range(THREAD_MAX_CNT):
			t = Process(target=startMongo)
			tlist.append(t)
			t.start()

		for i in range(THREAD_MAX_CNT):
			tlist[i].join()

	except Exception, msg:
		print msg

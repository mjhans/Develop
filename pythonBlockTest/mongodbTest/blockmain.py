#!/usr/bin/env python
#coding=utf8

import os
from threading import Thread
from  mongo import *

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
		startMongo()
		startMongo()
		startMongo()
		startMongo()
		startMongo()

		startMongo()
		startMongo()
		startMongo()
		startMongo()
		startMongo()

	except Exception, msg:
		print msg

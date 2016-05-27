#!/usr/bin/env python
#coding=utf8

import os
from threading import Thread
from  mongo import *

##########################################################################################
if __name__ == "__main__":
	tlist = list()
	try:
		conn = mongodbconn()
		mongobulkInsert(conn)
		mongoInsert(conn)
	except Exception, msg:
		print msg

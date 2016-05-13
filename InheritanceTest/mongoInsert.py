#!/usr/bin/env python
#coding=utf8

__author__ = 'mjhans'

##########################################################################################
# Import
##########################################################################################

from pymongo import MongoClient
from datetime import datetime
from multiprocessing import Process, current_process
import random
from store.ConnectionPoolManager import *
dummydata = [
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4},
	{"test1": 0, "test2": 1, "test3": 2, "test4": 3, "test5": 4}
]

class insertMongoData(object):

	#=====================================================================================
	def __init__(self):
		self.count = 0
		self.conn = None
		self.plist = list()
		self.pool = None
		pass
	#=====================================================================================
	def initMongoConnPool(self):
		try:
			ConnectionPoolManager.init(minCnt=10, maxCnt=20, host='127.0.0.1', port=27017)
		except Exception, msg:
			raise Exception("dbexception")

	#=====================================================================================
	def insertDataPool(self, dataList, cnt):
		i = 0
		cur = current_process()
		print "Current process name : %s" % cur.name
		sts = datetime.now()
		conn = ConnectionPoolManager.getDBConn()
		conn2 = conn.cnx
		print conn2
		while i < cnt:
			key = "test:%d" % i
			conn2["TEST"].test.insert({key : dataList})
			i += 1
		ets = datetime.now()
		ConnectionPoolManager.freeDBConn(conn)
		print "%s, elapsed time : %s" % (cur.name, (ets-sts))

	#=====================================================================================
	def initMongoConn(self):
		try:
			self.conn = MongoClient(host="127.0.0.1", port=27017, max_pool_size=100)
		except Exception, msg:
			raise Exception("dbexception")
	#=====================================================================================
	def insertData(self, dataList, cnt):
		i = 0
		cur = current_process()
		print "Current process name : %s" % cur.name
		conn2 = MongoClient(host="127.0.0.1", port=27017, max_pool_size=100)
		sts = datetime.now()
		while i < cnt:
			key = "test:%d" % i
			conn2["TEST"].test.insert({key : dataList})
			i += 1
		ets = datetime.now()
		conn2.close()
		print "%s, elapsed time : %s" % (cur.name, (ets-sts))

	#=====================================================================================
	def start(self):
		cnt = random.randint(1000, 9999)
		self.initMongoConn()
		self.insertData(dummydata, 10000)
		#self.initMongoConnPool()
		#self.insertDataPool(dummydata, 10000)

	#=====================================================================================
	def closeConn(self):
		try :
			self.conn.close()
		except Exception, msg:
			raise Exception("close Exception")

	#=====================================================================================
	def __repr__(self):
		return "insertCount : %d, conn : %s" % (self.count, self.conn)


##########################################################################################
if __name__ == '__main__':
	try:
		imd = insertMongoData()
		plist = list()

		for i in range(10):
			p = Process(target=imd.start)
			plist.append(p)
			p.start()

		for i in range(10):
			plist[i].join()


	except Exception, msg:
		print msg
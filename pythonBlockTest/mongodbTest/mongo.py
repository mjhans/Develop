#!/usr/bin/env python
#coding=utf8

import os
from datetime import datetime
import pymongo


##########################################################################################
def mongodbconn(host="127.0.0.1", port=27017):
	result = None
	try:
		result = pymongo.MongoClient(host=host, port=port)
	except Exception, msg:
		raise Exception(msg)
	return result

##########################################################################################
def mongoUpdate(conn):
	try:
		result = conn["TEST"].test.update({},{"$inc":{"t1":1, "t2" : -2}}, upsert=False, multi=True)
		#print result
	except Exception, msg:
		raise Exception(msg)

##########################################################################################
def mongobulkInsert(conn):
	try:
		bulk = conn["TEST"].test.initialize_ordered_bulk_op()
		bulk.find({}).remove()
		sts = datetime.now()
		for i in range(100000):
			msg = "TestDB test col, index %d" % i
			bulk.insert({"t1":i, "t2":i, "msg":msg})

		result = bulk.execute()
		ets = datetime.now()

		print "db bulk insert elapsed time : %s" % (ets - sts)

	except Exception, msg:
		raise Exception(msg)

##########################################################################################
def mongoInsert(conn):
	try:
		bulk = conn["TEST"].test
		bulk.remove(multi=True)
		sts = datetime.now()
		for i in range(100000):
			msg = "TestDB test col, index %d" % i
			bulk.insert({"t1":i, "t2":i, "msg":msg})

		ets = datetime.now()

		print "db insert elapsed time : %s" % (ets - sts)

	except Exception, msg:
		raise Exception(msg)


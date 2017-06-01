#!/usr/bin/env python
#coding=utf8
"""
====================================
:mod: 테스트용 non-blocking XML-RPC 서버
====================================
.. moduleauthor:: 채문창 <mcchae@gmail.com>
.. note:: GNU
설명
=====
테스트용 non-blocking XML-RPC 서버
"""

##########################################################################################
import time
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import pymongo

def mycoroutine():
	conn = pymongo.MongoClient("10.31.1.80", 27017)
	while True:
		pid, i = yield
		coll = conn["IDS_RTM_TRAFFIC"].ids_traffic_daily_dev.find()
		cnt = coll.count()
		p = open("/Users/mjhans/Documents/Dev/gitRepo/Develop/xmlrpctest/test.txt", mode='r')
		print "file : %s" % p.readlines()

		print "[%d] %d, count : %s" % (pid, i, cnt)

##########################################################################################
class TestSvc(object):
	def __init__(self):
		pass

	def ping(self, pid, _sleep=0):
		it = mycoroutine()
		next(it)
		for i in xrange(_sleep):
			it.send((pid, i,))
		return True

##########################################################################################
def doSvc():

	mgr = TestSvc()
	from SocketServer import ThreadingMixIn
	class SimpleThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
		pass
	class RequestHandler(SimpleXMLRPCRequestHandler):
		rpc_paths = ('/TestSvc')
	server = SimpleThreadXMLRPCServer(('0.0.0.0', 9000),
			                            requestHandler=RequestHandler,
			                            logRequests=False,
			                            allow_none=True,
	)
	server.register_introspection_functions()
	server.register_instance(mgr)
	server.serve_forever()

##########################################################################################
if __name__=='__main__':
	doSvc()
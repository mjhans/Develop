#!/usr/bin/env python
#coding=utf8
"""
====================================
:mod: 테스트용 blocking XML-RPC 서버
====================================
.. moduleauthor:: 채문창 <mcchae@gmail.com>
.. note:: GNU
설명
=====
테스트용 blocking XML-RPC 서버
"""

##########################################################################################
import time
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import pymongo
##########################################################################################
class TestSvc(object):

	def ping(self, pid, _sleep=0):
		conn = pymongo.MongoClient("10.31.1.80", 27017)
		for i in xrange(_sleep):
			coll = conn["IDS_RTM_TRAFFIC"].ids_traffic_daily_dev.find()
			cnt = coll.count()
			p = open("test.txt", mode='r')
			print "file : %s" % p.readlines()
			print "[%d] %d, count : %s" % (pid, i, cnt)
		return True

##########################################################################################
def doSvc():
	mgr = TestSvc()
	class RequestHandler(SimpleXMLRPCRequestHandler):
		rpc_paths = ('/TestSvc')
	server = SimpleXMLRPCServer(('0.0.0.0', 9000),
	                            requestHandler=RequestHandler,
	                            logRequests=False,
	                            allow_none=True,
	)
	server.register_introspection_functions()
	#server.register_instance(mgr)
	server.register_function(mgr.ping, "ping")
	server.serve_forever()

##########################################################################################
if __name__=='__main__':
	doSvc()
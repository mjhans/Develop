#!/usr/bin/env python
#coding=utf8
__author__ = 'mjhans'

from  tornado.ioloop import IOLoop
from tornado import gen
import tornado.web
from tornado.httpserver import HTTPServer
from tornado import gen
from tornado.netutil import  bind_sockets
from time import sleep
from datetime import datetime
import pymongo

def initMongo(_host = "127.0.0.1", _port=27017):
	_mongo = None
	try:
		_mongo = pymongo.MongoClient(host=_host, port = _port)
	except Exception, msg:
		raise Exception("init mongo exception : %s" % msg)

	return _mongo



##############################################################################
def doc_count(dbcursor):
	cnt = 0
	#_devinfos = dbcursor.find()
	for _dev in range(1000):
		cnt += 1
	return cnt

##############################################################################
class AsyncHandler(tornado.web.RequestHandler):

	mongo = None


	@gen.coroutine
	def async_callback(self, dbcursor):
		cnt = doc_count(dbcursor)
		raise gen.Return(cnt)


	#=========================================================================
	@gen.coroutine
	def get(self, *args, **kwargs):
		sts = datetime.now()
		if self.mongo == None:
			self.mongo = initMongo()
		dbctx = self.mongo["IDS_RTM_TRAFFIC"]
		cnt = yield (self.async_callback(dbctx["ids_traffic_daily_dev"]))
		ets = datetime.now()
		msg = "async elapsed time : %s, count : %s" % ((ets - sts), cnt)
		self.write(msg)
		self.finish()



	def post(self, *args, **kwargs):
		sts = datetime.now()
		print "post : %s" % self.request.body
		ets = datetime.now()
		self.write("Hello, world(post): %s" % (ets-sts))

	def put(self, *args, **kwargs):
		sts = datetime.now()
		print "put : %s" % self.request.body
		ets = datetime.now()
		self.write("Hello, world(put) : %s" % (ets-sts))

	def delete(self, *args, **kwargs):
		sts = datetime.now()
		print "delete %s" % self.request.query
		print "delete %s" % self.request.body
		ets = datetime.now()
		self.write("Hello, world(delete) : %s" % (ets-sts))



##############################################################################
class MainHandler(tornado.web.RequestHandler):

	mongo = None

	#=========================================================================
	def get(self, *args, **kwargs):
		sts = datetime.now()
		# if self.mongo == None:
		# 	self.mongo = initMongo(_host="10.31.1.240")
		#dbctx = self.mongo["IDS_RTM_TRAFFIC"]
		#cnt = doc_count(dbctx["ids_traffic_daily_dev"])
		cnt = doc_count([])
		ets = datetime.now()
		msg = "sync elapsed time : %s, count : %s" % ((ets-sts), cnt)
		self.write(msg)
		self.finish()

	def post(self, *args, **kwargs):
		sts = datetime.now()
		print "post : %s" % self.request.body
		ets = datetime.now()
		self.write("Hello, world(post): %s" % (ets-sts))

	def put(self, *args, **kwargs):
		sts = datetime.now()
		print "put : %s" % self.request.body
		ets = datetime.now()
		self.write("Hello, world(put) : %s" % (ets-sts))

	def delete(self, *args, **kwargs):
		sts = datetime.now()
		print "delete %s" % self.request.query
		print "delete %s" % self.request.body
		ets = datetime.now()
		self.write("Hello, world(delete) : %s" % (ets-sts))


##############################################################################
class Application(tornado.web.Application):

	#=========================================================================
	def __init__(self):
		handlers = [
			(r"/hello/synctest/?", MainHandler),
			(r"/hello/asynctest/?", AsyncHandler)
		]

		tornado.web.Application.__init__(self, handlers)


##############################################################################
def main():
	app = Application()
	server = HTTPServer(app)
	server.bind(8888)
	server.start(0)
	IOLoop.current().start()


##############################################################################
if __name__ == "__main__":
	main()


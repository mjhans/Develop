#!/usr/bin/env python
#coding=utf8

__author__ = 'mjhans'

##########################################################################################
# Import
##########################################################################################
import pymongo
import random
from UDException import *
##################################################################################
class MongoDBConnector(object):

	NAME = "Mongodb"
	#=====================================================================================
	def __init__(self, userid = "",
	             pssword="",
	             host="localhost",
	             port=27017,
	             db=""):
		"""
		:param userid: db사용자(optional)
		:param pssword: db 사용자 암호(optional)
		:param host: ip / url
			default : localhost
		:param port: db port
			default : 27017
		:param db:
		:return:
		"""
		self.name = "Mongodb"
		self.userid = userid
		self.passwd = pssword
		self.host = host
		self.port = port
		self.db = db
		self.cnx = None
		try:
			self.cnx = pymongo.MongoClient(host=host, port=port)
			self.id = random.random()
		except Exception, msg:
			raise DBConnectionException("DBConnection Error : %s, type : %s" % (msg, self.name))

	#=====================================================================================
	def isConnected(self):
		isconn = False
		try:
			if self.cnx in [None, 0]:
				isconn = False
			else:
				isconn = self.cnx.alive()
		except Exception, msg:
			isconn = False
		return isconn

	#=====================================================================================
	def getConn(self):
		return self.cnx
	#=====================================================================================
	def __del__(self):
		self.dbDisConnect()
	#=====================================================================================
	def dbDisConnect(self):
		"""
		데이터베이스 커넥션 변수, 커넥션 상태 확인
		데이터베이스 커넥션 종료
		커넥션 변수에 값이 없을경우
			DBConnectionException 발생 시킴
		커넥션 종료시 예외발생시
			DBConnectionException 발생 시킴
		:return None:
		"""
		try:
			if self.cnx.alive():
				self.cnx.close()
			else:
				raise DBConnectionException("DBConnection Closed yet...")
		except Exception, msg:
			#raise DBConnectionException(msg)
			print msg

##########################################################################################
if __name__ == "__main__":
	try:
		conn = MongoDBConnector()
		print conn.cnx
	except Exception, msg:
		print msg
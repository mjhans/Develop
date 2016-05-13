#!/usr/bin/env python
#coding=utf8

__author__ = 'mjhans'

import redis

##################################################################################
class DBConnector(object):

	NAME = "redis"
	#=====================================================================================
	def __init__(self, userid = "",
	             pssword="",
	             host="localhost",
	             port=6973,
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
		self.name = "redis"
		self.userid = userid
		self.passwd = pssword
		self.host = host
		self.port = port
		self.db = db
		self.cnx = None
		try:
			self.cnx = redis.Redis(host=host, port=port)
		except Exception, msg:
			raise Exception("DBConnection Error : %s, type : %s" % (msg, self.name))

	#=====================================================================================
	def getConnectionName(self):
		return "%s%s:%s" % (self.name, self.host, self.port)
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
				raise Exception("DBConnection Closed yet...")
		except Exception, msg:
			raise Exception(msg)

##########################################################################################
if __name__ == "__main__":
	try:
		conn = DBConnector()
		print conn.cnx
	except Exception, msg:
		print msg
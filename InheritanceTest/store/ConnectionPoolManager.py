#!/usr/bin/env python
#coding=utf8

__author__ = 'mjhans'

##########################################################################################
# Import
##########################################################################################
from MongoDBConnector import MongoDBConnector


class ConnectionPoolManager:
	"""
	DBCP 관리
	"""
	__dbConnPool_Use = []   # Connection List of Use
	__dbConnPool_Free = []   # Connection List of Free
	__minConnCnt = 3         # 최소연결 유지 갯수
	__maxConnCnt = 3         # 최대연결 유지 갯수

	__dbKind = ""  # DB종류
	__userId = ""  # db사용자
	__pssword = ""  # db사용자암호
	__host = "127.0.0.1"  # ip/url
	__port = 270107  # Port
	__db = ""  # db

	#=====================================================================================
	@staticmethod
	def init(minCnt=3, maxCnt=3, dbKind='',userId='', pssword='', host="127.0.0.1", port=27017, db=''):
		"""
		초기화
		:param minCnt: 최소 생성 갯수(해당갯수만큼 시작시 생성한다.)
		:param maxCnt: 최대 생성 갯수
		"""
		ConnectionPoolManager.__minConnCnt = minCnt
		ConnectionPoolManager.__maxConnCnt = maxCnt

		ConnectionPoolManager.__dbKind = dbKind  # DB종류
		ConnectionPoolManager.__userId = userId  # db사용자
		ConnectionPoolManager.__pssword = pssword  # db사용자암호
		ConnectionPoolManager.__host = host  # ip/url
		ConnectionPoolManager.__port = port  # Port
		ConnectionPoolManager.__db = db  # db

		# connection pool 생성
		for i in range(ConnectionPoolManager.__minConnCnt):
			conn = ""
			try :
				conn = MongoDBConnector(host=ConnectionPoolManager.__host, port= ConnectionPoolManager.__port)

				if conn.isConnected() :
					ConnectionPoolManager.__dbConnPool_Free.append(conn)
				else :
					del conn
			except Exception as ue:  # 사용자 정의 EXCEPTION 실행
				del conn


	#=====================================================================================
	@staticmethod
	def getDBConn():
		"""
		Connection얻기
		"""
		if ConnectionPoolManager.freeCnt() > 0 :
			# 사용할 것이 있는 경우에는 Free Connect를 전달한다.
			readyDBConn = ConnectionPoolManager.__dbConnPool_Free.pop(0)
			if readyDBConn.isConnected() :
				ConnectionPoolManager.__dbConnPool_Use.append(readyDBConn)
				# print ConnectionPoolManager.useCnt(), ConnectionPoolManager.freeCnt()
				return readyDBConn
			else :
				del readyDBConn
				return ConnectionPoolManager.getDBConn()
		else :
			# Free Connect가 남지 않아서 사용할 내용이 없는 경우
			if (ConnectionPoolManager.useCnt()+ConnectionPoolManager.freeCnt()) >= ConnectionPoolManager.__maxConnCnt : # 연결한 갯수가 사용가능갯수 이상으로 된 경우에는
				# print ConnectionPoolManager.useCnt(), ConnectionPoolManager.freeCnt()
				return Exception
			else :
				readyDBConn = ""
				try:
					# 새로운 연결을 만들어서 돌려준다.
					readyDBConn = MongoDBConnector(host=ConnectionPoolManager.__host, port= ConnectionPoolManager.__port)
					if readyDBConn.isConnected():
						ConnectionPoolManager.__dbConnPool_Use.append(readyDBConn)
						# print ConnectionPoolManager.useCnt(), ConnectionPoolManager.freeCnt()
						return readyDBConn
					else:
						del readyDBConn
				except Exception as ue:  # 사용자 정의 EXCEPTION 실행
					del readyDBConn
					# print ConnectionPoolManager.useCnt(), ConnectionPoolManager.freeCnt()
					return Exception
		pass
	#=====================================================================================
	@staticmethod
	def freeDBConn(readyDBConn):
		"""
		Connection
		:param conn: 돌려줄 connection
		"""
		if (ConnectionPoolManager.useCnt() + ConnectionPoolManager.freeCnt()) > ConnectionPoolManager.__minConnCnt:
			# 연결한 갯수가 사용가능갯수 이상으로 된 경우에는 반환한 것은 해제한다.
			for i in range(ConnectionPoolManager.useCnt()) :
				conn = ConnectionPoolManager.__dbConnPool_Use[i]
				if conn.id == readyDBConn.id :
					freeCon = ConnectionPoolManager.__dbConnPool_Use.pop(ConnectionPoolManager.__dbConnPool_Use.index(conn))
					# if conn == freeCon :
					# 	print "equal conn"
					# else :
					# 	print "notEqual conn"
					freeCon.dbDisConnect()        # 연결요청을 해지한다.
					# print 1234
					del freeCon
					# print ConnectionPoolManager.useCnt(), ConnectionPoolManager.freeCnt()

					return
		else :
			for i in range(ConnectionPoolManager.useCnt()) :
				conn = ConnectionPoolManager.__dbConnPool_Use[i]
				if conn.id == readyDBConn.id :
					tmpConn = ConnectionPoolManager.__dbConnPool_Use.pop(ConnectionPoolManager.__dbConnPool_Use.index(conn))
					ConnectionPoolManager.__dbConnPool_Free.append(tmpConn)
					# print ConnectionPoolManager.useCnt(), ConnectionPoolManager.freeCnt()
					return



	#=====================================================================================
	@staticmethod
	def useCnt():
		"""
		사용하는 Connection 갯수
		"""
		return len(ConnectionPoolManager.__dbConnPool_Use)


	#=====================================================================================
	@staticmethod
	def freeCnt():
		"""
		사용하지 않는 Connection 갯수
		"""
		return len(ConnectionPoolManager.__dbConnPool_Free)

	#=====================================================================================
	@staticmethod
	def toString():
		return ConnectionPoolManager.__userId
	
	##########################################################################################
if __name__ == '__main__':
		import time
	# try :
		sleepTerm = 0.5
		ConnectionPoolManager.init(minCnt=10, maxCnt=20, host='127.0.0.1', port=27017)
		# for i in range(100) :
		# 	con10 = ConnectionPoolManager.getDBConn()
		# 	time.sleep(2)
		# 	ConnectionPoolManager.freeDBConn(con10)
		# 	time.sleep(2)
		# con11 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# con12 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# con9 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# con8 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# con7 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# con6 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# cona1 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# cona2 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# ConnectionPoolManager.freeDBConn(con6)
		# time.sleep(sleepTerm)
		# ConnectionPoolManager.freeDBConn(con7)
		# time.sleep(sleepTerm)
		# ConnectionPoolManager.freeDBConn(con8)
		# time.sleep(sleepTerm)
		# ConnectionPoolManager.freeDBConn(con9)
		# time.sleep(sleepTerm)
		# ConnectionPoolManager.freeDBConn(con11)
		# time.sleep(sleepTerm)
		# ConnectionPoolManager.freeDBConn(con12)
		# time.sleep(sleepTerm)
		# cona2 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# cona2 = ConnectionPoolManager.getDBConn()
		# time.sleep(sleepTerm)
		# cona2 = ConnectionPoolManager.getDBConn()

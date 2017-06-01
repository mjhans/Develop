#!/usr/bin/env python
#coding=utf8

__author__ = 'mjhans'

from multiprocessing import Process, log_to_stderr, JoinableQueue

from threading import Thread
import select
import logging
import heapq
import marshal
import socket
from datetime import datetime
from time import sleep
import signal

import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

PORT = 3000

class UDPProcess(Process):
	#=====================================================================================
	def __init__(self, que):
		Process.__init__(self)
		self.port = PORT
		self.stopped = False
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.settimeout(1)
		self.sock.bind(('0.0.0.0', self.port))
		self.q = que
		self.pktcnt = 0
	#=====================================================================================
	def run(self):
		try:
			while not self.stopped:
				try:
					i_r,w_r,e_r = select.select([self.sock],[],[],1000)
					for s in i_r:
						if s == self.sock:
							self.pktcnt += 1
							recvData, address = self.sock.recvfrom(1500)
							if recvData is None :
								continue

							self.recvProc(recvData, address)

							if self.pktcnt % 1000 == 0:
								print "Process[%d]:pktcnt=%s" % (self.port, self.pktcnt)
				except socket.timeout:
					continue
				except Exception,e:
					sleep(1)
					print "Process[%d] Except : %s" % (self.port,e.message)
					self.stop()
					#continue
		except KeyboardInterrupt, msg:
			print "KeyboardInterrupt : %s" % msg
		finally:
			self.stop()
	#=====================================================================================
	def recvProc(self, msg, addr):
		dict = {}
		dict['data'] = msg
		dict['addr'] = addr[0]
		#msg = marshal.dumps(dict)
		self.q.put(dict)

	#=====================================================================================
	def stop(self):
		self.stopped = True

	#=====================================================================================
	def close(self):
		self.stopped = True
		self.sock.close()
		# self.stop()

################################################################################
class UDPWorker(Process):
	#=====================================================================================
	def __init__(self, que):
		Process.__init__(self)
		self.port = PORT
		self.stopped = False
		self.q = que
		self.msgcnt = 0
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#=====================================================================================
	def run(self):
		try:
			while not self.stopped:
				try:
					data = self.q.get()
					self.recvProc(data)
					self.q.task_done()
					self.msgcnt += 1
					if self.msgcnt % 1000 == 0:
						print "FSUDPProcess[%d]:msgcnt=%s" % (self.port, self.msgcnt)
				except Exception, e:
					sleep(1)
					print "Worker Exception : %s" % e
					#self.stop()
					continue
		except KeyboardInterrupt, msg:
			print "KeyboardInterrupt : %s" % msg
		finally:
			self.stop()

	#=====================================================================================
	def recvProc(self, data):
		try :
			#print "received data : %s" % data
			self.sock.sendto(data['data'], (data['addr'], PORT +1))
		except Exception, msg:
			print msg

	#=====================================================================================
	def stop(self):
		self.stopped = True
	#=====================================================================================
	def close(self):
		self.stopped = True
		# self.stop()

##########################################################################################
if __name__ == '__main__':
	log_to_stderr(logging.DEBUG)

	mq = JoinableQueue()
	Pnum = 5
	try:

		proc = UDPProcess(mq)
		proc.start()

		worker = UDPWorker(mq)
		worker.start()

		try:
			proc.join()
			worker.join()

			mq.close()
			mq.join_thread()
		except KeyboardInterrupt, msg :
			print "KeyboardInterrupt : %s" % msg
	finally:
		print ""

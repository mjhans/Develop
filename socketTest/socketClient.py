#!/usr/bin/env python
#coding=utf8

__author__ = 'mjhans'

import socket
import datetime
import sys
from multiprocessing import Process, current_process

PORT = 3000
UDP_IP = "127.0.0.1"

def communicate(sock):
	server_address = (UDP_IP, PORT)
	#print 'connecting to %s port %s' % server_address
	sts = datetime.datetime.now()
	for i in xrange(5000):
		msg = "test Message%s" % i
		sock.sendto(msg, server_address)
		data, addr = sock.recvfrom(1024)
	ets = datetime.datetime.now()
	print "process id : %s, elapsed time : %s" % (current_process().name, (ets - sts))


##########################################################################################
if __name__ == '__main__':
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Connect the socket to the port where the server is listening

	proc = list()
	try:
		sock.bind((UDP_IP, PORT + 1))
		for i in range(20):
			p = Process(target=communicate, args=(sock,))
			proc.append(p)
			p.start()

		for i in range(20):
			proc[i].join()
	except Exception, msg:
		print "socket exception : %s" % msg



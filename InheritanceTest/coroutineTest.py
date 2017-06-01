#!/usr/bin/env python
#coding=utf8

#=====================================================================================
def coroutine(func):
	def start(*args, **kwargs):
		cr = func(*args, **kwargs)
		cr.next()
		return cr
	return start

class myreturn(Exception):
	def __init__(self, value):
		self.value = value

def delegate():
	yield 1
	yield 2

def composed():
	yield 'A'
	for value in delegate():
		yield value
	yield {"test":0, "test2":1}

#=====================================================================================
@coroutine
def testCoroutine1():
	while True:
		crname, r, anotherCo = yield
		for idx in range(r):
			print "coroutine name : %s, index : %d" % (crname, idx)
			anotherCo.send(idx)

#=====================================================================================
def testGenerator(cnt):
	print "Counting down from : %s" % cnt
	while cnt > 0:
		yield cnt
		cnt -= 1

#=====================================================================================
@coroutine
def testCoroutine2():
	idx = 0
	while True:
		t = yield
		idx += 1
		print "testco2 : %s, index : %d" % (t, idx)

##########################################################################################
if __name__ == '__main__':
	# it = testCoroutine1()
	# it2 = testCoroutine2()
	# it.send(("co1", 100, it2,))

	it = composed()
	print next(it)
	print it.send(1)
	print it.send(1)
	print it.send(1)

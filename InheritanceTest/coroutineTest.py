#!/usr/bin/env python
#coding=utf8

#=====================================================================================
def coroutine(func):
	def start(*args, **kwargs):
		cr = func(*args, **kwargs)
		cr.next()
		return cr
	return start

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
	# it2.send("******************************")
	# it.send(("co2", 100, it2,))
	x = testGenerator(10)
	print x.next()
	print x.next()
	print x.next()
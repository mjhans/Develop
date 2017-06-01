__author__ = 'mjhans'


import time

def get(f):
	print f
	def method(*args, **kwargs):
		print "i am decorator get"
		after = f(*args, **kwargs)
		print after
		return after
	return method

class obja(object):
	def get(self):
		print "obja"

class objb(obja):

	@get
	def test(self):
		print "self.test : %s" % self.test
		print "objb test"

if __name__ == "__main__":
	o = objb()

	o.get()
	o.test()
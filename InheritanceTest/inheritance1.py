#!/usr/bin/env python
#coding=utf8

__author__ = 'mjhans'

##########################################################################################
# Import
##########################################################################################

##################################################################################
class foo(object):
	NAME = "unknown"
	NAME2 = "u"
	#=====================================================================================
	def __init__(self, name):
		self.NAME = name

	#=====================================================================================
	def getName(self):
		return (self.NAME, self.NAME2)

	def setName(self, n2):
		self.NAME2 = n2

	#=====================================================================================
	@staticmethod
	def setStaticName(n2):
		foo.NAME2 = n2

	#=====================================================================================
	@classmethod
	def setClassName(cls, n2):
		cls.NAME2 = n2

class bar(foo):
	pass

##########################################################################################
if __name__ == '__main__':
	f = foo("test")
	f.setName("foo2")
	print f.getName(), foo.NAME2
	f.setStaticName("fooStatic")
	print f.getName(), foo.NAME2
	f.setClassName("fooClass")
	print f.getName(), foo.NAME2

	b = bar("bar")
	b.setName("bar2")
	print b.getName(), bar.NAME2, foo.NAME2
	b.setStaticName("barStatic")
	print b.getName(), bar.NAME2, foo.NAME2
	b.setClassName("barClass")
	print b.getName(), bar.NAME2, foo.NAME2
#!/usr/bin/env python
#coding=utf8
import os
import xmlrpclib
proxy = xmlrpclib.ServerProxy("http://localhost:9000/TestSvc")
print "[%d] TestSvc.ping(5)=%s" % (os.getpid(), proxy.ping2(os.getpid(), 100))
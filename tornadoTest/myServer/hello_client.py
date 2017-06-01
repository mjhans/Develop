#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mjhans'


import httplib
import urllib
import json


if __name__ == "__main__":
	params = json.dumps({"name":"tete", "address":"add"})
	headers = {"Content-Type": "application/json"}
	conn = httplib.HTTPConnection("localhost:8888")

	conn.request('GET','/hello/test', params, headers)
	resp = conn.getresponse()
	data = resp.read()
	print "status : %s" % resp.status
	print "data : %s" % data

	conn.request('GET','/hello/test2', params, headers)
	resp = conn.getresponse()
	data = resp.read()
	print "status : %s" % resp.status
	print "data : %s" % data

	conn.request('POST','/hello/test', params, headers)
	resp = conn.getresponse()
	data = resp.read()
	print "status : %s" % resp.status
	print "data : %s" % data

	conn.request('POST','/hello/test2', params, headers)
	resp = conn.getresponse()
	data = resp.read()
	print "status : %s" % resp.status
	print "data : %s" % data

	conn.request('PUT','/hello/test', params, headers)
	resp = conn.getresponse()
	data = resp.read()
	print "status : %s" % resp.status
	print "data : %s" % data

	conn.request('DELETE','/hello/test', params, headers)
	resp = conn.getresponse()
	data = resp.read()
	print "status : %s" % resp.status
	print "data : %s" % data
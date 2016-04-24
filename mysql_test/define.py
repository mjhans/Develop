#!/usr/bin/env python
#coding=utf8

DATABASE="gTest"
TABLENAME = "gCreateLogTable"

IP = "192.168.99.102"
UID = "root"
PASSWORD="r"

DATAPATH = "/Users/mjhans/Dev/FW/"
FILENAME = "fwlog_%s.csv"


LOAD_INFILE = """LOAD DATA LOCAL INFILE '%s' INTO TABLE %s
FIELDS TERMINATED BY '\\t'
LINES TERMINATED BY '\\n'
"""
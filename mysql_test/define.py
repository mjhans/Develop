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
( timestamp ,
clock       ,
event       ,
ip_type      ,
name         ,
sip          ,
sip1         ,
sip2         ,
sip3         ,
sport        ,
dip          ,
dip1         ,
dip2         ,
dip3         ,
dport        ,
nat_sip      ,
nat_sip1     ,
nat_sip2     ,
nat_sip3     ,
nat_sport    ,
nat_dip      ,
nat_dip1     ,
nat_dip2     ,
nat_dip3     ,
nat_sport    ,
nat_dip      ,
nat_dip1     ,
nat_dip2     ,
nat_dip3     ,
nat_dport    ,
protocol     ,
direction    ,
pkt_id       ,
spd_id       ,
nat_id       ,
action       ,
tcp_flag     ,
inpacket     ,
outpacket    ,
inbytes      ,
outbytes     ,
url          ,
userid       ,
status       ,
holding_time ,
sid          ,
profile_name ,
retrans_count,
url_category ,
iface        ,
description  )
"""
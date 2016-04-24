#!/usr/bin/env python
#coding=utf8

import mysql.connector as mariadb

from define import *
from listners import InsListner


def createdb(cursor):
    sql = "CREATE DATABASE IF NOT EXISTS %s;" % DATABASE
    return cursor.execute(sql)

def createTable(cursor):
    """
    :param cursor:
    :return:
    """
    sql = """
CREATE TABLE IF NOT EXISTS %s (
id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
timestamp double not null,
clock integer DEFAULT '0'               NOT NULL,
event int(10) unsigned not null,
ip_type int(10) unsigned not null,
name varchar(256),
sip int(10) unsigned not null,
sip1 int(10) unsigned,
sip2 int(10) unsigned,
sip3 int(10) unsigned,
sport smallint(5) unsigned not null,
dip int(10) unsigned not null,
dip1 int(10) unsigned,
dip2 int(10) unsigned,
dip3 int(10) unsigned,
dport smallint(5) unsigned not null,
nat_sip int(10) unsigned,
nat_sip1 int(10) unsigned,
nat_sip2 int(10) unsigned,
nat_sip3 int(10) unsigned,
nat_sport smallint(5) unsigned,
nat_dip int(10) unsigned,
nat_dip1 int(10) unsigned,
nat_dip2 int(10) unsigned,
nat_dip3 int(10) unsigned,
nat_dport smallint(5) unsigned,
protocol tinyint(3) unsigned not null,
direction tinyint(3) unsigned,
pkt_id smallint(5) unsigned,
spd_id int(10) unsigned not null,
nat_id int(10) unsigned,
action smallint(5) unsigned,
tcp_flag smallint(5) unsigned,
inpacket bigint(20) unsigned,
outpacket bigint(20) unsigned,
inbytes bigint(20) unsigned,
outbytes bigint(20) unsigned,
url varchar(256),
userid varchar(256),
status smallint(5) unsigned,
holding_time int(10) unsigned,
sid int(10) unsigned,
profile_name int(10) unsigned,
retrans_count int(10) unsigned,
url_category int(10) unsigned,
iface varchar(10),
description varchar(256),
PRIMARY KEY(id, clock),
INDEX index1(timestamp),
INDEX index2(event),
INDEX index3(ip_type),
INDEX index4(sip),
INDEX index5(sport),
INDEX index6(dip),
INDEX index7(dport),
INDEX index8(protocol),
INDEX index9(spd_id)) ENGINE = MYISAM
""" % TABLENAME
    return cursor.execute(sql)
##########################################################################################
if __name__ == '__main__':
    try:
        cnx = mariadb.connect(user=UID, password=PASSWORD, host=IP)
        cursor = cnx.cursor()
        createdb(cursor)
        cnx.database  = DATABASE
        createTable(cursor)
        ins = InsListner()
        ins.start()

    except Exception, msg:
        print msg
    finally:
        try:
            cnx.close()
        except Exception, msg:
            print msg

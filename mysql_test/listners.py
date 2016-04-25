#!/usr/bin/env python
#coding=utf8


# pip install watchdog
import time
from datetime import datetime, timedelta
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import mysql.connector as mariadb

from define import *


class DataHandler(FileSystemEventHandler):

    def __init__(self):
        self.runcount = 0
        self.cumulate_timediff = timedelta(0)

    def process(self, event):
        print "Got it!"
        print event.src_path, event.event_type
        self.runcount += 1

        bulk_sql = LOAD_INFILE % (event.src_path, TABLENAME)
        #print bulk_sql

        try:
            cnx = mariadb.connect(user=UID, password=PASSWORD, host=IP, database=DATABASE)
            cursor = cnx.cursor()
            sts = datetime.now()
            cursor.execute("SET autocommit = 0")
            cursor.execute(bulk_sql)
            cnx.commit()
            ets = datetime.now()

            self.cumulate_timediff += (ets-sts)
            print """\
during time : %s
inserted total row : %s
time diff : %s
time per 1 row : %s
time per 10,000 row : %s
""" %\
((ets -sts),
(self.runcount * 20000),
self.cumulate_timediff,
(self.cumulate_timediff / (self.runcount * 20000)),
(self.cumulate_timediff / ((self.runcount * 20000)) * 10000))
        except Exception, msg:

            print msg
        finally:
            os.remove(event.src_path)
            cnx.close()

    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        "self.process(event)"

class InsListner(object):
    def __init__(self):
        ""
    def start(self):
        event_handler = DataHandler()
        observer = Observer()
        observer.schedule(event_handler, path=DATAPATH, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(0.05)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == "__main__":
    lis = InsListner()
    lis.start()
#!/usr/bin/env python
#coding=utf8


# pip install watchdog
import time
from datetime import datetime
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import mysql.connector as mariadb

from define import *


class DataHandler(FileSystemEventHandler):

    def process(self, event):
        print "Got it!"
        print event.src_path, event.event_type

        bulk_sql = LOAD_INFILE % (event.src_path, TABLENAME)
        print bulk_sql

        try:
            cnx = mariadb.connect(user=UID, password=PASSWORD, host=IP, database=DATABASE)
            cursor = cnx.cursor()
            #cursor.execute("")
            sts = datetime.now()
            cursor.execute(bulk_sql)
            cnx.commit()
            ets = datetime.now()

            print """ \
during time : %s
time per 1 row : %s
            """ % ((ets -sts),(ets-sts) / 18150)
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
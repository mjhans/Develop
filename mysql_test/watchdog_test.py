#!/usr/bin/env python
#coding=utf8

import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print "Got it!"
        print event


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(0.05)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
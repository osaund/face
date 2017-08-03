import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import datetime


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        subprocess.call(['python','converters.py'])
        print "Files created in dist at: " + datetime.datetime.now().isoformat()


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='src', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
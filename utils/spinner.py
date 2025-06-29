import threading
import itertools
import sys
import time

class Spinner:
    def __init__(self, msg="Scanning ..."):
        self.spinner = itertools.cycle(['|', '/', '-', '\\'])
        self.stop_running = False
        self.msg = msg

    def start(self):
        def spin():
            while not self.stop_running:
                sys.stdout.write(f"\r{self.msg} {next(self.spinner)}")
                sys.stdout.flush()
                time.sleep(0.1)
        threading.Thread(target=spin).start()

    def stop(self):
        self.stop_running = True
        sys.stdout.write("\rDone!            \n")

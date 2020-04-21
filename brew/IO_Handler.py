import TILT_IO
import threading
import time

class iohandler:

    running = True

    def __init__(self,IOdata):
        self.IOdata = IOdata
        self.tilt = TILT_IO.tiltio(self.IOdata)
        self.tilt.funcRun()

    def funcRun(self):
        threading.Thread(target=self._funcRun).start()

    def _funcRun(self):
        while (self.running == True):
            time.sleep(1)
        self.tilt.running = False


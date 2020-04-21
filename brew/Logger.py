import os
import threading
import time
from datetime import datetime, date

class logging:

    #logging scan rate (seconds)
    scan = 3600
    running = True

    def __init__(self,IOdata):
        self.IOdata = IOdata
        self.readConfig()
        if os.path.exists('logs') == False:
            os.mkdir('logs')

    def readConfig(self):
        if os.path.exists('logging.conf') == False:
            return
        f = open('logging.conf','r')
        for line in f:
            fields = line.split('=')
            if (fields[0] == 'scan'):
                self.scan = fields[1]

    def logRun(self):
        threading.Thread(target=self._logRun).start()

    def _logRun(self):
        print("brew logging activated")
        starting = True
        while self.running:
            fname = "logs/{}.csv".format(date.today().strftime("%Y%m%d"))
            f = open(fname,'a')
            if os.path.exists(fname) == False:
                f.write("time,temp,SG")
            if (starting == False):
                dstr = datetime.now().strftime("%H%M%S")
                line = "{},{},{}\n".format(dstr,format(self.IOdata.temp, '.2f'),self.IOdata.sg)
                f.write(line)
            f.close()
            starting = False

            current = datetime.now().hour
            while current == datetime.now().hour:
                if self.running == False:
                    break
                time.sleep(1)
        print("brew logging stopped")
        self.cleanup()

    def cleanup(self):
        pass
    

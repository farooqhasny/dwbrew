import ProdCon
from time import sleep
import json
import threading

class server:

    scan = 1;
    running = True
    
    def __init__(self,IOdata):
        self.IOdata = IOdata
        self.producer = ProdCon.producer()
        
    def serverRun(self):
        threading.Thread(target=self._serverRun).start()

    def _serverRun(self):
        while self.running:
            obj = {"temp":self.IOdata.temp,"sg":self.IOdata.sg}
            self.producer.send(json.dumps(obj))
            sleep(1)

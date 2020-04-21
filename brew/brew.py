import IO_Handler
import Logger
import brewview
import IOData
import server
import time
from datetime import datetime

IOdata = IOData.IOData()

iohandler = IO_Handler.iohandler(IOdata);
iohandler.funcRun()

log = Logger.logging(IOdata)
log.logRun()

view = brewview.view(IOdata)
view.logRun()

server = server.server(IOdata)
server.serverRun()

running = True;

try:
    while True:
        current = datetime.now().minute
        while current == datetime.now().minute:
            if running == False:
                break
            time.sleep(1)
        dstr = datetime.now().strftime("%H%M%S")
        line = "{},{},{}\n".format(dstr,format(IOdata.temp, '.2f'),IOdata.sg)
        print(line)
except KeyboardInterrupt:
    running = False
    iohandler.running = False
    log.running = False
    view.running = False


              

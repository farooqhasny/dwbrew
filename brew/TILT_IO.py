import blescan
import sys
import requests
import datetime
import time
import bluetooth._bluetooth as bluez
import os
import threading

class tiltio:

    running = True

    #The default device for bluetooth scan. If you're using a bluetooth dongle you may have to change this.
    dev_id = 0

    def __init__(self,IOdata):
        self.IOdata = IOdata

    def funcRun(self):
        threading.Thread(target=self._funcRun).start()

    #scan BLE advertisements until we see one matching our tilt uuid
    def _funcRun(self):
        try:
                sock = bluez.hci_open_dev(self.dev_id)

        except:
                print ("error accessing bluetooth device...")
                sys.exit(1)

        blescan.hci_le_set_scan_parameters(sock)
        blescan.hci_enable_le_scan(sock)

        while (self.running == True):

                returnedList = blescan.parse_events(sock, 10)

                for beacon in returnedList: #returnedList is a list datatype of string datatypes seperated by commas (,)
                        output = beacon.split(',') #split the list into individual strings in an array
                        if output[0] == 'd4:54:01:07:45:60':
                                #print('device found')
                                self.IOdata.temp = (float(output[2])-32)*5/9 #convert the string for the temperature to a float type
                                self.IOdata.sg = float(output[3])/1000

        blescan.hci_disable_le_scan(sock)


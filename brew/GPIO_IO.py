import time
import threading
import ASUS.GPIO as GPIO
import threading

class gpio_io:

        running = True

        def __init__(self,IOdata):
                self.IOdata = IOdata

        def funcRun(self):
                #print("Starting ultrasonics")
                threading.Thread(target=self._funcRun).start()

        def _funcRun(self):
                GPIO.setmode(GPIO.BOARD)
                Trigger_AusgangsPin = 7
                Echo_EingangsPin    = 8
                sleeptime = 0.8
                GPIO.setup(Trigger_AusgangsPin, GPIO.OUT)
                GPIO.setup(Echo_EingangsPin, GPIO.IN)
                GPIO.output(Trigger_AusgangsPin, False)
                prev = -1;
                AusschaltZeit = 0;

                while self.running:
                        GPIO.output(Trigger_AusgangsPin, True)
                        time.sleep(0.00001)
                        GPIO.output(Trigger_AusgangsPin, False)

                        EinschaltZeit = time.time()
                        while GPIO.input(Echo_EingangsPin) == 0:
                                EinschaltZeit = time.time() # Es wird solange die aktuelle Zeit gespeichert, bis das Signal aktiviert wird
                        while GPIO.input(Echo_EingangsPin) == 1:
                                AusschaltZeit = time.time() # Es wird die letzte Zeit aufgenommen, wo noch das Signal aktiv war

                        Dauer = AusschaltZeit - EinschaltZeit
                        self.IOdata.level = (Dauer * 34300) / 2
                        time.sleep(sleeptime)
	 

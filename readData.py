import ASUS.GPIO as GPIO
import spidev
import math
import json
import time

def ReadChannel(channel, spi):
        adc = spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data

def ConvertVolts(data,places):
        volts = (data * 3.3) / float(1023)
        volts = round(volts,places)
        return volts

def ConvertTemp(data,places):
        #temp = math.log10(((10240000/data)-10000))
        #temp = 1/(0.001129148 + (0.000234125 + (0.0000000876741 *temp*temp))*temp)
        temp = -0.2*data + 399.6
        temp = temp-273.15
        temp = round(temp,places)
        return temp

def readLevel():
        try:
                GPIO.setWarnings(False)
                GPIO.setmode(GPIO.BOARD)
                Trigger_AusgangsPin = 7
                Echo_EingangsPin    = 8
                GPIO.setup(Trigger_AusgangsPin, GPIO.OUT)
                GPIO.setup(Echo_EingangsPin, GPIO.IN)
                GPIO.output(Trigger_AusgangsPin, False)
                AusschaltZeit = 0;

                GPIO.output(Trigger_AusgangsPin, True)
                time.sleep(0.00001)
                GPIO.output(Trigger_AusgangsPin, False)

                EinschaltZeit = time.time()
                while GPIO.input(Echo_EingangsPin) == 0:
                        EinschaltZeit = time.time() # Es wird solange die aktuelle Zeit gespeichert, bis das Signal aktiviert wird
                while GPIO.input(Echo_EingangsPin) == 1:
                        AusschaltZeit = time.time() # Es wird die letzte Zeit aufgenommen, wo noch das Signal aktiv war

                Dauer = AusschaltZeit - EinschaltZeit
                Abstand = (Dauer * 34300) / 2
                return Abstand
        except:
                return 0
         

def readData():
	try:
                spi = spidev.SpiDev()
                light_channel = 0
                temp_channel  = 1
                spi.open(2,0)
                spi.max_speed_hz=1000000
                        
                light_level = ReadChannel(light_channel,spi)
                light_volts = ConvertVolts(light_level,2)
                light_lumin = 1024-light_level
                
                # Read the temperature sensor data
                temp_level = ReadChannel(temp_channel,spi)
                temp_volts = ConvertVolts(temp_level,2)
                temp = ConvertTemp(temp_level,2)

                return {"temp":temp,"light":light_lumin}
	except:
		return {"temp":-1,"light":-1}

def getValues():
        try:
                level = readLevel()
                data = readData()
                return {"temp":data["temp"],"light":data["light"],"level":level}
        except:
                return {}

#retStr = getValues()
#print(retStr)

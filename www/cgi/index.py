#!/usr/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()
import json
import ProdCon
from time import sleep

consumer = ProdCon.consumer()

resp = None
while resp == None:
    resp = consumer.receive()
    sleep(1)
    continue

# Print necessary headers.
print("Content-Type: text/html")
print("")
print(resp)

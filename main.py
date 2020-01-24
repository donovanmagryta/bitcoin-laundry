import urequests
import network
import time
import machine
from machine import Pin
relay = Pin(12, Pin.OUT)

import ConnectWiFi
ConnectWiFi.connect()
print ('booting up')
while True:
  checkbal = urequests.get('')
  time.sleep(15)
  recheckbal = urequests.get('')
  if checkbal < recheckbal:
      if recheckbal - checkbal > 0.001:
        relay.value(1)
        time.sleep(15)
  else:
     relay.value(0)
  
  
      

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
  checkbal = urequests.get('http://blockchain.info/api/q/addressbalance/1EzwoHtiXB4iFwedPr49iywjZn2nnekhoj?confirmations=6')
  time.sleep(13)
  recheckbal = urequests.get('http://blockchain.info/api/q/addressbalance/1EzwoHtiXB4iFwedPr49iywjZn2nnekhoj?confirmations=6')
  if checkbal < recheckbal:
      if recheckbal - checkbal > 0.001:
        relay.value(1)
        time.sleep(13)
  else:
     relay.value(0)
  
  
      

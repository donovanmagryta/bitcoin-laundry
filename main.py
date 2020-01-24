import urequests
import network
import time
import machine
from machine import Pin
relay = Pin(12, Pin.OUT)
import ConnectWiFi
ConnectWiFi.connect()
while True:
  checkbal = urequests.get('http://blockchain.info/api/q/addressbalance/14wRAXh2Qrm84vUwuJ4N9xzUw6WXtqC6eR?confirmations=6')
  checkbal = int(checkbal)
  time.sleep(13)
  recheckbal = urequests.get('http://blockchain.info/api/q/addressbalance/14wRAXh2Qrm84vUwuJ4N9xzUw6WXtqC6eR?confirmations=6')
  recheckbal = int(recheckbal)
  if (checkbal < recheckbal):
      if (recheckbal - checkbal > 0.001):
          relay.value(1)
          time.sleep(600)
  else:
     relay.value(0)

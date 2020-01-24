address = ""
url = "https://blockchain.info/q/addressbalance/" + address + "?confirmations=6"
import urequests
import network
import time
import machine
from machine import Pin
relay = Pin(12, Pin.OUT)
import ConnectWiFi
ConnectWiFi.connect()
while True:
  checkbal = urequests.get(url)
  checkbal = float(checkbal)
  time.sleep(13)
  recheckbal = urequests.get(url)
  recheckbal = float(recheckbal)
  if (recheckbal > checkbal):
      if (recheckbal - checkbal > 0.0002):
          relay.value(1)
          time.sleep(600)
  else:
     relay.value(0)

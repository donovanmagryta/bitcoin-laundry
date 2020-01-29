
deviceid = "1"
mode = "paypal"
address = "na"
delay = "13"
ontime = "600"
amount = "0.25"
host = "http://example.com"
ipnfilename = "/paypalipn.php"
if (mode == "bitcoin"):
  url = "https://blockchain.info/q/addressbalance/" + address + "?confirmations=6"
if (mode == "paypal"):
  url = host + ipnfilename + "?iot=" + deviceid
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
  print(url)
  checkbal = (checkbal.text)
  checkbal = float(checkbal)
  print(checkbal)
  time.sleep(delay)
  recheckbal = urequests.get(url)
  recheckbal = (recheckbal.text)
  recheckbal = float(recheckbal)
  print(recheckbal)
  if (recheckbal > checkbal):
    if (recheckbal - checkbal >= amount):
      print("payment received")
      relay.value(1)
      time.sleep(ontime)
      print("on for 600 seconds")
  else: 
     relay.value(0)
     print("off")

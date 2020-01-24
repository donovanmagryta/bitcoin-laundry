
import urequests
import network
import time
import machine
import neopixel
import ConnectWiFi
ConnectWiFi.connect()
print ('booting up')
while True:
  checkbal = urequests.get('https://blockchain.info/balance?active=$address')
  time.sleep(5)
  recheckbal = urequests.get('https://blockchain.info/balance?active=$address')
  if checkbal < recheckbal:
  
  
      

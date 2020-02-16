# bitcoin-laundry
Bitcoin powered appliances using Sonoff Basic, MicroPython firmware, and Blockchain.info plain text API

OR

Paypal powered using Sonoff Basic, MicroPython firmware, PHP web host, and PayPal IPN service



SETUP:


1. GET PARTS

get a sonoff basic, wire strippers, screwdriver, USB to TTL adapter, and female jumper wires, header pins, soldering iron, solder.


2. SOFTWARE PREP

Download anaconda python distribution and make sure to enable "add to path".

Download uPyCraft.

3. HARDWARE PREP

solder header pins onto Sonoff to enable connection to USB-to-TTL-adapter.
connect USB to serial adapter to sonoff.


4. FIRMWARE INSTALL

flash micropython with anaconda python from windows cmd prompt:

(replace COM11 with your usb port and replace micropython.bin with your micropython firmware filename)

conda install -c conda-forge esptool

cd Desktop

esptool.py --chip esp8266 erase_flash

esptool.py --chip esp8266 --port COM11 write_flash --flash_mode dout --flash_size detect 0x0 micropython.bin

5. ADJUST CODE PARAMETERS

edit parameters in each scripts: 

edit bitcoin address in main.py if you are not using paypal.

edit mode in main.py

for bitcoin mode, delay parameter must set to be greater than 13 seconds or else blockchain.info's API will reject queries.

Edit device id name in that file.

Edit WiFi credentials in connectWiFi.py

Edit website URL to match your web host site in both all files.

Edit paypal email in paypalbutton.php file to match your paypal business account email.

6. UPLOAD CODE

using upycraft, enable webrepl.

connect using webrepl.

Upload the preferred .py files to your sonoff.

For paypal, Upload both .php files to your web host.

7. SETUP PAYPAL

in paypal business account settings, point ipn calls to your /paypalipn.php url.

The payment URL must end in "?iot=" and then your switch's selected device ID number. For example: https://example.com/paypalbutton.php?iot=1




Appliance examples: microwave ovens, coffee makers, mood lighting, vending machines.

Bitcoin mode untested as of 1/24/2020
Paypal mode confirmed working as of 1/29/2020

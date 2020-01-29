# bitcoin-laundry
Bitcoin powered appliances using Sonoff Basic, MicroPython firmware, and Blockchain.info plain text API
OR
Paypal powered using Sonoff Basic, PHP server and PayPal IPN.

Flash micropython firmware onto Sonoff switch.

Rename bitcoin.py to "main.py" if you want to use BTC instead of paypal.

Edit device id name in that file.

Edit WiFi credentials in connectWiFi.py

Edit website URL to match your web host site in both all files.

Edit email in paypalbutton.php file to match your paypal business account email.

Upload the preferred .py files to your sonoff.

For paypal, Upload .php files to your web host.

The payment URL must end in "?iot=" and then your switch's selected device ID number. For example: https://example.com/paypalbutton.php?iot=1




Appliance examples: microwave ovens, coffee makers, mood lighting, vending machines.

Bitcoin mode untested as of 1/24/2020
Paypal mode confirmed working as of 1/29/2020


1. solder header pins onto Sonoff to enable connection to USB-to-TTL-adapter.

2. flash micropython with anaconda python from windows cmd prompt:

(replace COM11 with your usb port and replace micropython.bin with your micropython firmware filename)

conda install -c conda-forge esptool

cd Desktop

esptool.py --chip esp8266 erase_flash

esptool.py --chip esp8266 --port COM11 write_flash --flash_mode dout --flash_size detect 0x0 micropython.bin



3. open uPycraft.exe and connect to sonoff via usb.

4. setup WEBREPL in uPycraft to enable wireless script uploads.

5. modify parameters in scripts to match your info.

6. upload php scripts to your web host.

7. upload main.py and connectwifi.py to Sonoff using WEBREPL connection.

8. setup ipn calls in your paypal business account to point to your paypalipn.php url.

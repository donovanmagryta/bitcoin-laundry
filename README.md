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

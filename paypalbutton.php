<?php
$iot = urldecode($_GET["iot"]);
$return = urldecode($_GET["returned"]);
if ($return == "returned") {
 echo "Payment Received. Device will activate within 15 seconds.";
}
else {
echo "<h3>Pay to activate machine #</h3>";
echo $iot;
echo '<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
  <input type="hidden" name="business" value="torchiveinc@gmail.com">
  <input type="hidden" name="no_shipping" value="0">
  <input type="hidden" name="cmd" value="_xclick">
  <input type="hidden" name="amount" value="0.25">
  <input type="hidden" name="currency_code" value="USD">
  <input type="hidden" name="return" value="http://tipscale.digital/paypalbutton.php?returned=returned">
  <input type="hidden" name="custom" value="'.$iot.'">
  <input type="hidden" name="cm" value="'.$iot.'">
  <input type="hidden" name="item_name" value="device ID # '.$iot.'">
  <input type="hidden" name="item_number" value="'.$iot.'">
  <input name="notify_url" value="http://tipscale.digital/paypalipn.php" type="hidden">
  <input type="image" name="submit" border="0"
  src="https://www.paypalobjects.com/en_US/i/btn/btn_buynow_LG.gif"
  alt="Buy Now">
  <img alt="" border="0" width="1" height="1"
  src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif">
</form>';
}
?>

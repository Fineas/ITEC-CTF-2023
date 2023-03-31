
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $_SERVER['REQUEST_URI'] === '/flag' && $_COOKIE['flag'] === 'true' && $_COOKIE['cookie2'] === 'give it') {
  echo "Poftim: \n";
  echo file_get_contents('flag.txt');
} else {
  highlight_file(__FILE__);
}
?>

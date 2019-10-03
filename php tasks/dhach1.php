<?php

$rates = array(2, 4, 5, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6);
$middleRate = array_sum($rates)/count($rates);

echo "Сердний балл Анона = $middleRate";

?>
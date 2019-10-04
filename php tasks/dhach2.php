<?php
$anon = 174;
$schoolmates = [168,
                179,
                188,
                193,
                182,
                174,
                173,
                170,
                211,
               ];

$tallThatAnon = 0;

foreach ($schoolmates as $schoolmate) {
    if ($anon < $schoolmate) {
        $tallThatAnon++;
    }
}

echo "\nВ классе всего $tallThatAnon учеников выше, чем Анон";
?>
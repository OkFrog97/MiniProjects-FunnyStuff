<?php

$find = array(
    'fuck',
    'idiot',
    'bitch'
);

$replace = array(
    'f**k',
    'i***t',
    'b**ch'
);

$userInput = 'This bitch muther fuck looks like an idiot';

echo str_ireplace($find, $replace, $userInput);
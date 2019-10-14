<?php

function strFinder ($array){
    /*
    This function return all string elements of given array.
    Code:
    > $exampleArray = array("Hello", true, 12, "banana", 42, "world"); 
    > $strFromExampleArray = strFinder($exampleArray);
    > print_r ($strFromExampleArray);
    Output:
    > Array (
            [0] => "Hello",
            [1] => "banana",
            [2] => "world",
            )
    */
    
    
    
    
    
    
    foreach ($array as $element) {
        if is_string($element){
            
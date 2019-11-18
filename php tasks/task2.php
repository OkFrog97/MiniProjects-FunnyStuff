<?php
    /*Написать функцию, которая принимает в качестве аргументов префикс и массив строк и возвращает все строки, начинающиеся с указанного префикса. Необходимо реализовать функцию наиболее оптимальным образом.*/
    
    function pref_mutch($pref, $words_list){
        
        $matches = array();
        $regexp = "/$pref/ui";
        
        foreach ($words as $word){
            if (preg_match($regexp, $word)){
                array_push($matches, $word);
            }
        }
        
        return $matches;
    }
?>
<?php
    /*
    Реализовать скрипт на PHP, который определит является ли год високосным.
    На вход скрипту нужно передавать значение, скрипт должен выдавать один из возможных ответов: ДА, НЕТ, ОШИБКА ВО ВХОДНЫХ ДАННЫХ.
    Реализовать в виде веб-страницы с формой для передачи значения. Обязательно с использованием ajax.
    */


    function is_leap ($year){
        /*Get year:str and check is in leap.
        Return error if year can't convert to int or input year is earlier when gregorian calendar was start used.*/
        if (strcasecmp(gettype($year), "integer") == 0 or $year < 1600){
            return "ОШИБКА ВО ВХОДНЫХ ДАННЫХ";
            }
        elseif (($year % 4 == 0 && $year % 100 != 0) || $year % 400 == 0){
            return "ДА";
            }
        return "НЕТ";
        }

    $year = $_GET["val"];

    echo is_leap($year);
?>
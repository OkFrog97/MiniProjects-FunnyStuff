<?php
$answers = array(
    "Да",
    "Нет",
    "Возможно",
    "Скорее нет, чем да",
    "Посже",
    "Спроси завтра",
);

$genAnswerKey = array_rand($answers);

echo "Ответ на твой вопрос: $answers[$genAnswerKey]";
?>
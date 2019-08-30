
  $answer = $name[0].".";
 
  for ($i = 0; $i < mb_strlen($name); $i++){
      if ($name[$i] === " "){
          $answer = $answer.$name[$i+1];
          }
  }
  return strtoupper($answer);
}
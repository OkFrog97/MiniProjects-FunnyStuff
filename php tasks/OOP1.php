<?php

class Entree {
  public $name;
  public $ingredients =  array();
  public function hasIngredients ($ingredients) {
      return in_array($ingredients, $this->ingredients);
    }
}

$soup = new Entree;
$soup->name = 'Chicken soup';
$soup->ingredients = array('chicken','salt','maggie','whater');

foreach (['salt','papper','chicken'] as $ing){
    if ($soup->hasIngredients($ing)){
        print "Soup has $ing.\n";
    }
}

?>
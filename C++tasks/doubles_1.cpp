#include <iostream>
#include <math.h>

int main() {
  
  double a,b,c,p,s;
  
  /*input vars*/
  std::cin >> a >> b >> c;
  p = (a+b+c)/2;
  
  /*Gerone formul*/
  s = sqrt(p*(p-a)*(p-b)*(p-c));
  
  /*output answer*/
  std::cout << s;
  
  return 0;
}
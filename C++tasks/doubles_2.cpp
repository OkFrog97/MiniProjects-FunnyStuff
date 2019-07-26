#include <iostream>
#include <cmath>
int main() {
  double x;
  std::cin >> x;
  std::cout << trunc(((x-(int)x/1)*10));
  return 0;
}
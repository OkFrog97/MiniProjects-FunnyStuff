#include <iostream>

int main() {
  int p, x, y, yy;
  std::cin >> p >> x >> y;
  yy = x * p % 100;
  x = x + x * p / 100;
  y = y + y * p / 100 + yy;
  x = x + y / 100;
  y = y % 100;
  std::cout << x << " " << y;
  return 0;
}
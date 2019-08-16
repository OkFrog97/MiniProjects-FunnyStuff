#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
  // put your code here
  double count=0, sum=0, digit;
  std::cin >> digit;
  while (digit != 0) {
    sum = sum + digit;
    count++;
    std::cin >> digit;
  }
  std::cout << std::setprecision(11) << sum/count;
  return 0;
}
#include <iostream>

int main() {
  int N, temp, f1=0, f2=1, count=1;
  std::cin >> N;
  
  while (N!=count){
    temp = f2;
    f2 = f2 + f1;
    f1 = temp;
    count ++;
  }
  
  std::cout << f2;
  
  return 0;
}
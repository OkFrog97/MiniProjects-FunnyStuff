#include <iostream>

int main() {
  int N, temp, f1 = 0, f2 = 1, count = 1;
  std::cin >> N;
  
  while (f2<N){
    temp = f2;
    f2 = f2 + f1;
    f1 = temp;
    count ++;
    if (f2==N)std::cout << count;
    else if(f2>N)std::cout << -1;
  }
  
  return 0;
}
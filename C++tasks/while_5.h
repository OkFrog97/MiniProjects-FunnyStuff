#include <iostream>

int main() {
   int N, big = 0, bigest = 0;
  
   std::cin >> N;
   if (N!=0&&bigest<N) bigest  = N;
   while (N!=0) {
       std::cin >> N;
       if (N!=0&&bigest<N) { 
           big = bigest;
           bigest  = N;
       }
       else if (N!=0&&bigest>=N&&big<N) big = N;
   }
   std::cout << big;
  return 0;
}
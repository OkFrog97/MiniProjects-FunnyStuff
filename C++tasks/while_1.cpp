#include <iostream>
using namespace std;

int main() {
  int i, N, x;
  cin >> N;
  i = 1;
  
  while (x<N){
      x = i*i;
      if (x<N) {
          cout << x << " ";
      }
      else {
          break;
      }
      i++;
  }
  
  return 0;
}
#include <iostream>
using namespace std;

int main() {
  int N, x=2;
  cin >> N;
  
  while (N%x!=0)
  {
    x++;
  }
  
  cout << x;
  return 0;
}
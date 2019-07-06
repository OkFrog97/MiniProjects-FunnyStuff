#include <iostream>
using namespace std;

int main() {
  int N, bin=1;
  cin >> N;
  while (bin<=N)
  {
    cout << bin << " ";
    bin = bin * 2;
  }
  return 0;
}
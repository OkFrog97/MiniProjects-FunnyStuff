#include <iostream>
using namespace std;

int main() {
  int v, t, mkad;
  mkad = 109;
  cin >> v >> t;
  cout << ((v*t)%mkad+mkad)%mkad;
  return 0;
}
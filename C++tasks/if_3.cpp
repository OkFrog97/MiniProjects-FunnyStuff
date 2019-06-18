#include <iostream>
using namespace std;

int main() {
  int x, y, z;
  cin >> x >> y >> z;
  if (y<=x && z<=x){
      cout << x;
  }
  else if (x<=y && z<=y) {
      cout << y;
  }
  else {
      cout << z;
  }
  return 0;
}
#include <iostream>
using namespace std;

int main() {
  int N, M, tmp, x, y, x2, y2;
  
  cin >> N >> M >> x >> y;
  
  if (N>M) {
   tmp = N;
   N = M;
   M = tmp;
  }
  
  x2 = M - y;
  y2 = N - x;
  
  if (x<y&&x<x2&&x<y2) {
   cout << x;
   }
  else if (y<x&&y<x2&&y<y2) {
   cout << y;
   }
  else if (x2<x&&x2<y&&x2<y2) {
   cout << x2;
   }
  else {
   cout << y2;
 }
  return 0;
}
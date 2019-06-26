#include <iostream>
using namespace std;

int main() {
  int a1,b1,a2,b2;
  cin >> a1 >> b1 >> a2 >> b2;
  
  if (a2-a1==b2-b1 || a2-a1==(b2-b1)*-1 || a2==a1 || b2==b1){
    cout << "YES";
  }
  else {
    cout << "NO";
  }
  
  return 0;
  return 0;
}
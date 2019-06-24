#include <iostream>
using namespace std;

int main() {
  int nextStlb, nextStr, myStlb, myStr;
  cin >> nextStlb >> nextStr >> myStln >> myStr;
  
  if (nextStlb==myStlb-1 || nextStlb==myStlb+1) {
      if (nextStr==myStr+2 || nextStr==myStr-2) {
          cout << "YES";
      }
      else{
          cout << "NO";
      }
  }
  else if (nextStlb==myStlb-2 || nextStlb==myStlb+2) {
      if (nextStr==myStr+1 || nextStr==myStr-1) {
          cout << "YES";
      }
      else {
          cout << "NO";
      }
  }
  else {
      cout << "NO";
  }
  return 0;
}
#include <iostream>
using namespace std;

int main() {
  int nextStlb, nextStr, myStlb, myStr;
  cin >> nextStlb >> nextStr >> myStlb >> myStr;
  
  if (nextStlb==myStlb+1 || nextStlb==myStlb-1 || nextStlb==myStlb){
      if (nextStr==myStr || nextStr==myStr-1 || nextStr==myStr+1){
          cout <<"YES";
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
#include <iostream>
#include <vector>

using namespace std; 

int main() {
  int a;
  cin >> a;
  vector <int> n(a);
  for (int i = 0; i < a; i++){
      cin >> n[i];
  }
  for (int i = 0; i < a; i = i + 2){
      cout << n[i] << " ";
  }
  return 0;
}
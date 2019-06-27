#include <iostream>
using namespace std;

int main() {
  int N, M, K;
  cin >> N >> M >> K;
  
  if ((K<N*M)&&(K>=N||K>=M)&&(K%N==0||K%M==0)) {
      cout << "YES";
  }
  else {
      cout << "NO";
  }
    
  return 0;
}
#include <iostream>
using namespace std;

int main() {
  int N, hstrN = 0, count = 1, hstrCount = 1;
  cin >> N;
  while (N!=0){
    if (hstrN==N){
      count ++;
      if (hstrCount<count) hstrCount=count;
    }
    else count = 1;
    hstrN=N;
    cin >> N;
  }
  std::cout << hstrCount;
  return 0;
}
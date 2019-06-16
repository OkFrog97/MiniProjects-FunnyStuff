#include <iostream>
using namespace std;

int main() {
  int sec;
  cin >> sec;

  int h = sec/3600;
  int h1 =(sec/3600)%24;
    
  int m = (sec%3600)/60;
  int m1 = m/10;
  int m2 = m%10;
  
  int s = sec - (h*3600 + m*60);
  int s1 = s/10;
  int s2 = s%10;
    
  cout << h1 <<":"<< m1 << m2 <<":"<< s1 << s2;
  return 0;
}
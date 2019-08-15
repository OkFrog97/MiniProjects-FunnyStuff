#include <iostream>

using namespace std;

int main() {
    int p, yy, x, y, k, i = 0;
    cin >> p >> x >> y >> k;
    while (i < k) {
        yy = x * p % 100;
        x = x + x * p / 100;
        y = y + y * p / 100 + yy;
        x = x + y / 100;
        y = y % 100;
        i = i + 1;
    }
    cout << x << " " << y;
    return 0;
}
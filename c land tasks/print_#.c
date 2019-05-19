#include <stdio.h>

int main () {
    for (int i = 1; i <= 5; i++){
        for (int hashNum = 1; hashNum <= 6 - i; hashNum ++){
            printf("#");
        }
        printf("\n");
    }
}
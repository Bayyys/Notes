#include <stdio.h>
#include <iostream>

#define XNAME(n) x##n
#define PXN(n) printf("x" #n " is %d\n", XNAME(n))

int main() {
    int XNAME(1) = 14;  // int x1 = 14;
    PXN(1);  // x1 is 14
  return 0;
}
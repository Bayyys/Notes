#include <stdio.h>
#include <iostream>

using namespace std;

#define PSQR(x) printf("The square of " #x " is %d\n", ((x) * (x)))

int main() {
  int x = 5;
  PSQR(x); // The square of x is 25
  PSQR(3 + 4); // The square of 3 + 4 is 49
  return 0;
}
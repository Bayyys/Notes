#include <stdio.h>
#include <iostream>

#define PR(...) printf(__VA_ARGS__)

int main() {
    int wt=1,sp=2;
    PR("hello\n");
    //输出：hello
    PR("weight = %d, shipping = %d",wt,sp);
    //输出：weight = 1, shipping = 2
    return 0;
}
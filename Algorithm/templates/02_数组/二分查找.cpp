#include <bits/stdc++.h>
using namespace std;

int binarySearch(int arr[], int l, int r, int target) {
  while (l <= r) {  // 边界 [left, right]
    int m = l + (r - l) / 2;
    // int m = r - l >> 1 + l;    // 位运算优先级低于加减法
    if (arr[m] > target)
      r = m - 1;
    else if (arr[m] < target)
      l = m + 1;
    else
      return m;
  }
  return -1;  // 未找到
}

int binarySearch(int arr[], int l, int r, int target) {
  while (l < r) {  // 边界 [left, right)
    int m = l + (r - l) / 2;
    if (arr[m] > target)
      r = m;
    else if (arr[m] < target)
      l = m + 1;
    else
      return m;
  }
  return -1;  // 未找到
}

int main() { return 0; }
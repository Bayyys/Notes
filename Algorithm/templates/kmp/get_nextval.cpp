using namespace std;
#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <queue>
#include <set>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

void get_nextval(const string& pattern, vector<int>& nextval) {
  int j = 0, k = -1;
  nextval[0] = -1;
  while (j < (int)pattern.size() - 1) {
    if (k == -1 || pattern[j] == pattern[k])
    // pattern[j] 表示后缀的单个字符
    // pattern[k] 表示前缀的单个字符
    {
      j++;
      k++;
      if (pattern[j] != pattern[k])
        nextval[j] = k;
      else
        // 如果相等回溯后字符不变，所以nextval值是回溯后字符的nextval值
        nextval[j] = nextval[k];
    } else {
      k = nextval[k];
    }
  }
}

// 返回src在dst中从pos开始往后的位置下标，不存在就返回-1
int index_KMP(const string& src, const string& pattern, int pos = 0) {
  int i = pos, j = 0;
  vector<int> next(pattern.size());
  get_nextval(pattern, next);
  while (i < (int)src.size() && j < (int)pattern.size()) {
    if (j == -1 || src[i] == pattern[j]) {
      i++;
      j++;
    } else {
      j = next[j];
    }
  }
  if (j == (int)pattern.size())
    return i - j;
  else
    return -1;
}
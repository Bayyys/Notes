/*
 * @lc app=leetcode.cn id=28 lang=cpp
 * @lcpr version=30110
 *
 * [28] 找出字符串中第一个匹配项的下标
 */

// @lcpr-template-start
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
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
// @lcpr-template-end
// @lc code=start
class Solution {
 public:
  int strStr(string haystack, string needle) {
    if (needle.empty()) return 0;
    if (haystack.empty() || haystack.size() < needle.size()) return -1;
    int next[needle.size()];
    getNext(needle, next);
    int j = 0;
    for (int i = 0; i < haystack.size(); i++) {
      while (j > 0 && haystack[i] != needle[j]) {
        j = next[j - 1];
      }
      if (haystack[i] == needle[j]) {
        j++;
      }
      if (j == needle.size()) {
        return i - j + 1;
      }
    }
    return -1;
  }

  void getNext(const string& s, int* next) {
    int j = 0;
    next[0] = j;
    for (int i = 1; i < s.size(); i++) {
      while (j > 0 && s[i] != s[j]) {
        j = next[j - 1];
      }
      if (s[i] == s[j]) {
        j++;
      }
      next[i] = j;
    }
  }
};
// @lc code=end

/*
// @lcpr case=start
// "sadbutsad"\n"sad"\n
// @lcpr case=end

// @lcpr case=start
// "leetcode"\n"leeto"\n
// @lcpr case=end

 */

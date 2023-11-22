/*
 * @lc app=leetcode.cn id=459 lang=cpp
 * @lcpr version=30110
 *
 * [459] 重复的子字符串
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
  void getNext(int* next, const string& s) {
    int j = -1;
    next[0] = j;
    for (int i = 1; i < s.size(); i++) {
      while (j >= 0 && s[i] != s[j + 1]) j = next[j];
      if (s[i] == s[j + 1]) j++;
      next[i] = j;
    }
  }

  bool repeatedSubstringPattern(string s) {
    if (s.empty()) return false;
    int next[s.size()];
    getNext(next, s);
    int len = s.size();
    if (next[len - 1] != -1 && len % (len - next[len - 1] - 1) == 0)
      return true;
    return false;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "abab"\n
// @lcpr case=end

// @lcpr case=start
// "aba"\n
// @lcpr case=end

// @lcpr case=start
// "abcabcabcabc"\n
// @lcpr case=end

 */

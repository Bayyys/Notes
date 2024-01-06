/*
 * @lc app=leetcode.cn id=647 lang=cpp
 * @lcpr version=30112
 *
 * [647] 回文子串
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
  int countSubstrings(string s) {
    int res = 0;
    for (int i = 0; i < s.size(); i++) {
      res += count(s, i, i);
      res += count(s, i, i + 1);
    }
    return res;
  }

  int count(string& s, int l, int r) {
    int res = 0;
    while (l >= 0 && r < s.size() && s[l] == s[r]) {
      l--;
      r++;
      res++;
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "abc"\n
// @lcpr case=end

// @lcpr case=start
// "aaa"\n
// @lcpr case=end

 */

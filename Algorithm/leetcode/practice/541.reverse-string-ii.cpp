/*
 * @lc app=leetcode.cn id=541 lang=cpp
 * @lcpr version=30110
 *
 * [541] 反转字符串 II
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
  string reverseStr(string s, int k) {
    for (int i = 0; i < s.size(); i += (2 * k)) {
      if (i + k <= s.size()) {
        myReverse(s, i, i + k);
      } else {
        myReverse(s, i, s.size());
      }
    }
    return s;
  }

  void myReverse(string &s, int start, int end) {
    for (int i = start, j = end - 1; i < j; i++, j--) {
      swap(s[i], s[j]);
    }
  }
};
// @lc code=end

/*
// @lcpr case=start
// "abcdefg"\n2\n
// @lcpr case=end

// @lcpr case=start
// "abcd"\n2\n
// @lcpr case=end

 */

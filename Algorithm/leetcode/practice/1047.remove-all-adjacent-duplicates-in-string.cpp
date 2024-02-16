/*
 * @lc app=leetcode.cn id=1047 lang=cpp
 * @lcpr version=30110
 *
 * [1047] 删除字符串中的所有相邻重复项
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
  string removeDuplicates(string s) {
    string res = "";
    for (auto c : s) {
      if (res.empty() || res.back() != c) {
        res.push_back(c);
      } else {
        res.pop_back();
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "abbaca"\n
// @lcpr case=end

 */

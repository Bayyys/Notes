/*
 * @lc app=leetcode.cn id=1844 lang=cpp
 * @lcpr version=30110
 *
 * [1844] 将所有数字用字符替换
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
  string replaceDigits(string s) {
    for (int i = 0; i < s.size(); i += 2) {
      s[i + 1] = s[i] + s[i + 1] - '0';
    }
    return s;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "a1c1e1"\n
// @lcpr case=end

// @lcpr case=start
// "a1b2c3d4e"\n
// @lcpr case=end

 */

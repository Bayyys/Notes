/*
 * @lc app=leetcode.cn id=70 lang=cpp
 * @lcpr version=30112
 *
 * [70] 爬楼梯
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
  int climbStairs(int n) {
    if (n <= 2) return n;
    int dp[3] = {0, 1, 2};
    for (int i = 3; i <= n; i++) {
      int sum = dp[1] + dp[2];
      dp[1] = dp[2];
      dp[2] = sum;
    }
    return dp[2];
  }
};
// @lc code=end

/*
// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=123 lang=cpp
 * @lcpr version=30112
 *
 * [123] 买卖股票的最佳时机 III
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
  int maxProfit(vector<int>& prices) {
    // dp[i][0]: 第i天不持有股票的最高收益 = 0
    // dp[i][1]: 第i天持有第一次股票的最高收益 = max(dp[i-1][1], -prices[i])
    // dp[i][2]: 第i天卖出第一次股票的最高收益 = max(dp[i-1][2], dp[i-1][1] + prices[i])
    // dp[i][3]: 第i天持有第二次股票的最高收益 = max(dp[i-1][3], dp[i-1][2] - prices[i])
    // dp[i][4]: 第i天卖出第二次股票的最高收益 = max(dp[i-1][4], dp[i-1][3] + prices[i])
    vector<vector<int>> dp(2, vector<int>(5, 0));
    dp[0][1] = -prices[0];
    dp[0][3] = -prices[0];
    for (int i = 1; i < prices.size(); i++) {
      dp[i % 2][0] = 0;
      dp[i % 2][1] = max(dp[(i - 1) % 2][1],  -prices[i]);
      dp[i % 2][2] = max(dp[(i - 1) % 2][2], dp[(i - 1) % 2][1] + prices[i]);
      dp[i % 2][3] = max(dp[(i - 1) % 2][3], dp[(i - 1) % 2][2] - prices[i]);
      dp[i % 2][4] = max(dp[(i - 1) % 2][4], dp[(i - 1) % 2][3] + prices[i]);
    }
    return max(dp[(prices.size() - 1) % 2][2], dp[(prices.size() - 1) % 2][4]);
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,3,5,0,0,3,1,4]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [7,6,4,3,1]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

 */

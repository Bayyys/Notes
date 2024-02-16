/*
 * @lc app=leetcode.cn id=121 lang=cpp
 * @lcpr version=30112
 *
 * [121] 买卖股票的最佳时机
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
    // dp[i][0]: 第i天不持有股票的最高收益
    //          1. 第i-1天不持有股票: dp[i-1][0]
    //          2. 第i-1天持有股票，第i天卖出: dp[i-1][1] + prices[i]
    // dp[i][1]: 第i天持有股票的最高收益
    //          1. 第i-1天持有股票: dp[i-1][1]
    //          2. 第i-1天不持有股票，第i天买入:  - prices[i]
    vector<vector<int>> dp(2, vector<int>(2, 0));
    dp[0][0] = 0;
    dp[0][1] = -prices[0];
    for (int i = 1; i < prices.size(); i++) {
      dp[i % 2][0] = max(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1] + prices[i]);
      dp[i % 2][1] = max(dp[(i - 1) % 2][1], -prices[i]);
    }
    return dp[(prices.size() - 1) % 2][0];
  }
};
// @lc code=end

/*
// @lcpr case=start
// [7,1,5,3,6,4]\n
// @lcpr case=end

// @lcpr case=start
// [7,6,4,3,1]\n
// @lcpr case=end

 */

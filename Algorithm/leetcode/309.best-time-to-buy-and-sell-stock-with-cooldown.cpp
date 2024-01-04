/*
 * @lc app=leetcode.cn id=309 lang=cpp
 * @lcpr version=30112
 *
 * [309] 买卖股票的最佳时机含冷冻期
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
    // dp[i][0]: 第i天持有股票的最大收益(保持昨天状态/今天买入)
    //      = max(dp[i-1][0], dp[i-1][1] - prices[i], dp[i-1][3] - prices[i])
    // dp[i][1]: 第i天保持卖出状态(度过冷冻期)
    //      = max(dp[i-1][1], dp[i-1][3])
    // dp[i][2]: 第i天卖出股票的最大收益(今天卖出)
    //      = dp[i-1][0] + prices[i]
    // dp[i][3]: 第i天为冷冻期状态(昨天卖出)
    //      = dp[i-1][2]
    vector<vector<int>> dp(prices.size(), vector<int>(4, 0));
    dp[0][0] = -prices[0];
    for (int i = 1; i < prices.size(); i++) {
      dp[i][0] = max(dp[i - 1][0],
                     max(dp[i - 1][1] - prices[i], dp[i - 1][3] - prices[i]));
      dp[i][1] = max(dp[i - 1][1], dp[i - 1][3]);
      dp[i][2] = dp[i - 1][0] + prices[i];
      dp[i][3] = dp[i - 1][2];
    }
    return max(dp[prices.size() - 1][1], dp[prices.size() - 1][2]);
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3,0,2]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

 */

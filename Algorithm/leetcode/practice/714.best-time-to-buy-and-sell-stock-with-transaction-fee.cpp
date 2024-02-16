/*
 * @lc app=leetcode.cn id=714 lang=cpp
 * @lcpr version=30112
 *
 * [714] 买卖股票的最佳时机含手续费
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
  int maxProfit(vector<int>& prices, int fee) {
    vector<vector<int>> dp(2, vector<int>(2, 0));
    dp[0][0] = 0;  // 第i天不持有股票(保持昨天状态/今天卖出)
                   //      = max(dp[i-1][0], dp[i-1][1] + prices[i])
    dp[0][1] = -prices[0] -
               fee;  // 第i天持有股票(保持昨天状态/今天买入)
                     //      = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
    for (int i = 1; i < prices.size(); i++) {
      dp[i % 2][0] = max(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1] + prices[i]);
      dp[i % 2][1] =
          max(dp[(i - 1) % 2][1], dp[(i - 1) % 2][0] - prices[i] - fee);
    }
    return dp[(prices.size() - 1) % 2][0];
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1, 3, 2, 8, 4, 9]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,3,7,5,10,3]\n3\n
// @lcpr case=end

 */

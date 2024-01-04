/*
 * @lc app=leetcode.cn id=188 lang=cpp
 * @lcpr version=30112
 *
 * [188] 买卖股票的最佳时机 IV
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
  int maxProfit(int k, vector<int>& prices) {
    vector<vector<int>> dp(2, vector<int>(2 * k + 1, 0));
    for (int i = 1; i < 2 * k; i += 2) {
      dp[0][i] = -prices[0];
    }
    for (int i = 1; i < prices.size(); i++) {
      for (int j = 0; j < 2 * k - 1; j += 2) {
        dp[i % 2][j + 1] =
            max(dp[(i - 1) % 2][j + 1], dp[(i - 1) % 2][j] - prices[i]);
        dp[i % 2][j + 2] =
            max(dp[(i - 1) % 2][j + 2], dp[(i - 1) % 2][j + 1] + prices[i]);
      }
    }
    return dp[(prices.size() - 1) % 2][2 * k];
  }
};
// @lc code=end

/*
// @lcpr case=start
// 2\n[2,4,1]\n
// @lcpr case=end

// @lcpr case=start
// 2\n[3,2,6,5,0,3]\n
// @lcpr case=end

 */

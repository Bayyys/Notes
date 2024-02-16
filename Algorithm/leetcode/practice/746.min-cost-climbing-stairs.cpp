/*
 * @lc app=leetcode.cn id=746 lang=cpp
 * @lcpr version=30112
 *
 * [746] 使用最小花费爬楼梯
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
  int minCostClimbingStairs(vector<int>& cost) {
    /**
     * 1. 确定dp数组以及下标的含义: dp[i]表示爬到第i个台阶的最小花费
     * 2. 确定递推公式: dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
     * 3. dp数组如何初始化: dp[0] = cost[0], dp[1] = cost[1]
     * 4. 确定遍历顺序: 从前往后遍历
     * 5. 举例推导dp数组: 10 15 20
     */
    vector<int> dp(3);
    dp[0] = 0;
    dp[1] = 0;
    for (int i = 2; i <= cost.size(); i++) {
      dp[2] = min(dp[0] + cost[i - 2], dp[1] + cost[i - 1]);
      dp[0] = dp[1];
      dp[1] = dp[2];
    }
    return dp[2];
  }
};
// @lc code=end

/*
// @lcpr case=start
// [10,15,20]\n
// @lcpr case=end

// @lcpr case=start
// [1,100,1,1,1,100,1,1,100,1]\n
// @lcpr case=end

 */

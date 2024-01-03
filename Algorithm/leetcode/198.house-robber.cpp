/*
 * @lc app=leetcode.cn id=198 lang=cpp
 * @lcpr version=30112
 *
 * [198] 打家劫舍
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
  int rob(vector<int>& nums) {
    // dp[i]: 经过i间房子能偷到的最大金额
    // dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    vector<int> dp(nums.size() + 1, 0);
    if (nums.size() == 0) return 0;
    if (nums.size() == 1) return nums[0];
    dp[0] = nums[0];
    dp[1] = max(nums[0], nums[1]);
    for (int i = 2; i < nums.size(); i++) {
      dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
    }
    return dp[nums.size() - 1];
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3,1]\n
// @lcpr case=end

// @lcpr case=start
// [2,7,9,3,1]\n
// @lcpr case=end

 */

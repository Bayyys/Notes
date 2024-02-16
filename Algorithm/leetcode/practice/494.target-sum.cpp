/*
 * @lc app=leetcode.cn id=494 lang=cpp
 * @lcpr version=30112
 *
 * [494] 目标和
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
  int findTargetSumWays(vector<int>& nums, int target) {
    int sum = 0;
    for (auto num : nums) sum += num;
    if (sum < abs(target) || (sum + target) % 2 == 1) return 0;
    int bagSize = (sum + target) / 2;
    vector<int> dp(bagSize + 1, 0);
    dp[0] = 1;
    for (int i = 0; i < nums.size(); i++)
      for (int j = bagSize; j >= nums[i]; j--) dp[j] += dp[j - nums[i]];
    return dp[bagSize];
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,1,1,1,1]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1]\n1\n
// @lcpr case=end

 */

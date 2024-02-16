/*
 * @lc app=leetcode.cn id=213 lang=cpp
 * @lcpr version=30112
 *
 * [213] 打家劫舍 II
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
    if (nums.size() == 0) return 0;
    if (nums.size() == 1) return nums[0];
    int res1 = rob_helper(nums, 0, nums.size() - 2);
    int res2 = rob_helper(nums, 1, nums.size() - 1);
    return max(res1, res2);
  }

  int rob_helper(vector<int>& nums, int start, int end) {
    if (start == end) return nums[start];
    vector<int> dp(nums.size() + 1, 0);
    dp[start] = nums[start];
    dp[start + 1] = max(nums[start], nums[start + 1]);
    for (int i = start + 2; i <= end; i++) {
      dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
    }
    return dp[end];
  }
};
// @lc code=end

/*
// @lcpr case=start
// [2,3,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

 */

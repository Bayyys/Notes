/*
 * @lc app=leetcode.cn id=674 lang=cpp
 * @lcpr version=30112
 *
 * [674] 最长连续递增序列
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
  int findLengthOfLCIS(vector<int>& nums) {
    // dp[i]: 以nums[i]结尾的最长连续递增序列长度(包含nums[i])
    // = max(dp[i-1] + 1) if nums[i] > nums[i-1]
    vector<int> dp(nums.size(), 1);
    int res = 1;
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i - 1] < nums[i]) dp[i] = max(dp[i], dp[i - 1] + 1);
      if (dp[i] > res) res = dp[i];
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,3,5,4,7]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2,2,2]\n
// @lcpr case=end

 */

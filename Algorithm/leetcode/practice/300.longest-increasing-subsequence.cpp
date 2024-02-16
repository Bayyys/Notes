/*
 * @lc app=leetcode.cn id=300 lang=cpp
 * @lcpr version=30112
 *
 * [300] 最长递增子序列
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
  int lengthOfLIS(vector<int>& nums) {
    // dp[i]: 以nums[i]结尾的最长递增子序列长度(包含nums[i])
    // = max(dp[j] + 1) for j in [0, i) if nums[j] < nums[i]
    vector<int> dp(nums.size(), 1);
    int res = 1;
    for (int i = 1; i < nums.size(); i++) {
      for (int j = 0; j < i; j++) {
        if (nums[j] < nums[i]) dp[i] = max(dp[i], dp[j] + 1);
      }
      if (dp[i] > res) res = dp[i];
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [10,9,2,5,3,7,101,18]\n
// @lcpr case=end

// @lcpr case=start
// [0,1,0,3,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [7,7,7,7,7,7,7]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=416 lang=cpp
 * @lcpr version=30112
 *
 * [416] 分割等和子集
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
  bool canPartition(vector<int>& nums) {
    int sum = 0;
    for (auto num : nums) {
      sum += num;
    }
    if (sum % 2 == 1) return false;
    vector<int> dp(10001, 0);
    int target = sum / 2;
    for (int i = 0; i < nums.size(); i++) {
      for (int j = target; j >= nums[i]; j--) {
        dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]);
      }
    }
    if (dp[target] == target) return true;
    return false;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,5,11,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,5]\n
// @lcpr case=end

 */

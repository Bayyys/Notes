/*
 * @lc app=leetcode.cn id=718 lang=cpp
 * @lcpr version=30112
 *
 * [718] 最长重复子数组
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
  int findLength(vector<int>& nums1, vector<int>& nums2) {
    // dp[i][j]: 以nums1[i]和nums2[j]结尾的最长重复子数组长度
    // = dp[i-1][j-1] + 1 if nums1[i] == nums2[j]
    vector<vector<int>> dp(nums1.size(), vector<int>(nums2.size(), 0));
    int res = 0;
    for (int i = 0; i < nums1.size(); i++) {
      if (nums1[i] == nums2[0]) {
        dp[i][0] = 1;
        res = 1;
      };
    }
    for (int j = 0; j < nums2.size(); j++) {
      if (nums1[0] == nums2[j]) {
        dp[0][j] = 1;
        res = 1;
      }
    }
    for (int i = 1; i < nums1.size(); i++) {
      for (int j = 1; j < nums2.size(); j++) {
        if (nums1[i] == nums2[j]) dp[i][j] = dp[i - 1][j - 1] + 1;
        if (dp[i][j] > res) res = dp[i][j];
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3,2,1]\n[3,2,1,4,7]\n
// @lcpr case=end

// @lcpr case=start
// [0,0,0,0,0]\n[0,0,0,0,0]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=53 lang=cpp
 * @lcpr version=30111
 *
 * [53] 最大子数组和
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
  int maxSubArray(vector<int>& nums) {
    int res = INT32_MIN;
    int count = 0;  // 以nums[i]结尾的最大子数组和
    for (int i = 0; i < nums.size(); i++) {
      count += nums[i];
      res = max(res, count);
      if (count < 0) {  // 对后续加和起到副作用, 直接舍弃, 从下一个元素重新开始
        count = 0;
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [-2,1,-3,4,-1,2,1,-5,4]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

// @lcpr case=start
// [5,4,-1,7,8]\n
// @lcpr case=end

 */

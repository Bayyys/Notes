/*
 * @lc app=leetcode.cn id=15 lang=cpp
 * @lcpr version=30109
 *
 * [15] 三数之和
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
  vector<vector<int>> threeSum(vector<int>& nums) {
    vector<vector<int>> res;
    sort(nums.begin(), nums.end());  // 元素从小到大排序
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] > 0)
        break;  // 如果最小元素大于0，那么不可能有和为0的三元组, 直接返回
      // 对元素a进行去重 (找到最后一个a的位置)
      if (i > 0 && nums[i] == nums[i - 1]) continue;
      int left = i + 1, right = nums.size() - 1;
      while (left < right) {
        // a + b + c = 0
        // nums[i] + nums[left] + nums[right] = 0
        if (nums[i] + nums[left] + nums[right] < 0)
          left++;
        else if (nums[i] + nums[left] + nums[right] > 0)
          right--;
        else {
          res.push_back(vector<int>{nums[i], nums[left], nums[right]});
          // 进行去重操作
          while (right > left && nums[right] == nums[right - 1])
            right--;  // 找到第一个right的位置
          while (right > left && nums[left] == nums[left + 1])
            left++;         // 找到最后一个left的位置
          left++, right--;  // left right 同时收缩
        }
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [-1,0,1,2,-1,-4]\n
// @lcpr case=end

// @lcpr case=start
// [0,1,1]\n
// @lcpr case=end

// @lcpr case=start
// [0,0,0]\n
// @lcpr case=end

 */

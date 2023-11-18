/*
 * @lc app=leetcode.cn id=18 lang=cpp
 * @lcpr version=30109
 *
 * [18] 四数之和
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
  vector<vector<int>> fourSum(vector<int>& nums, int target) {
    vector<vector<int>> ans;
    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size(); i++) {
      // 剪枝处理
      if (nums[i] > target && nums[i] >= 0) break;
      // 去重操作
      if (i > 0 && nums[i] == nums[i - 1]) continue;
      for (int j = i + 1; j < nums.size(); j++) {
        // 剪枝处理
        if (nums[i] + nums[j] > target && nums[i] + nums[j] >= 0) break;
        if (j > i + 1 && nums[j] == nums[j - 1]) continue;
        int left = j + 1;
        int right = nums.size() - 1;
        while (right > left) {
          long sum =
              (long)nums[i] + nums[j] + nums[left] + nums[right];  // 防止溢出
          if (sum > target) {
            right--;
          } else if (sum < target) {
            left++;
          } else {
            ans.push_back({nums[i], nums[j], nums[left], nums[right]});
            while (right > left && nums[right] == nums[right - 1]) right--;
            while (right > left && nums[left] == nums[left + 1]) left++;
            right--;
            left++;
          }
        }
      }
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,0,-1,0,-2,2]\n0\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2,2,2]\n8\n
// @lcpr case=end

 */

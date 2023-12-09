/*
 * @lc app=leetcode.cn id=46 lang=cpp
 * @lcpr version=30111
 *
 * [46] 全排列
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
  vector<vector<int>> res;
  vector<int> path;
  void TV(vector<int>& nums, vector<bool>& us) {
    if (path.size() == nums.size()) {
      res.push_back(path);
      return;
    }
    for (int i = 0; i < nums.size(); i++) {
      if (us[i]) continue;
      us[i] = true;
      path.push_back(nums[i]);
      TV(nums, us);
      path.pop_back();
      us[i] = false;
    }
  }

  vector<vector<int>> permute(vector<int>& nums) {
    vector<bool> us(nums.size(), false);
    TV(nums, us);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [0,1]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

 */

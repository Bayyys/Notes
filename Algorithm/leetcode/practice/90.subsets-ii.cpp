/*
 * @lc app=leetcode.cn id=90 lang=cpp
 * @lcpr version=30111
 *
 * [90] 子集 II
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
  void TV(vector<int>& nums, int start) {
    res.push_back(path);
    for (int i = start; i < nums.size(); i++) {
      if (i > start && nums[i] == nums[i - 1]) {
        continue;
      }
      path.push_back(nums[i]);
      TV(nums, i + 1);
      path.pop_back();
    }
  }

  vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    TV(nums, 0);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [0]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=491 lang=cpp
 * @lcpr version=30111
 *
 * [491] 递增子序列
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
    if (path.size() >= 2) {
      res.push_back(path);
    }
    unordered_set<int> us;
    for (int i = start; i < nums.size(); i++) {
      if ((!path.empty() && nums[i] < path.back()) || us.count(nums[i])) {
        continue;
      }
      us.insert(nums[i]);
      path.push_back(nums[i]);
      TV(nums, i + 1);
      path.pop_back();
    }
  }

  vector<vector<int>> findSubsequences(vector<int>& nums) {
    TV(nums, 0);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [4,6,7,7]\n
// @lcpr case=end

// @lcpr case=start
// [4,4,3,2,1]\n
// @lcpr case=end

 */

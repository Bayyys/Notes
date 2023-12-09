/*
 * @lc app=leetcode.cn id=78 lang=cpp
 * @lcpr version=30111
 *
 * [78] 子集
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
    if (start >= nums.size()) {
      return;
    }
    for (int i = start; i < nums.size(); i++) {
      path.push_back(nums[i]);
      TV(nums, i + 1);
      path.pop_back();
    }
  }

  vector<vector<int>> subsets(vector<int>& nums) {
    TV(nums, 0);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [0]\n
// @lcpr case=end

 */

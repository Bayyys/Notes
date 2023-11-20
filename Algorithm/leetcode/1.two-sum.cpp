/*
 * @lc app=leetcode.cn id=1 lang=cpp
 * @lcpr version=30110
 *
 * [1] 两数之和
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
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map;  // <value, index>
    for (int i = 0; i < nums.size(); i++) {
      auto itertor = map.find(target - nums[i]);
      if (itertor != map.end()) {
        return {itertor->second, i};
      } else {
        map[nums[i]] = i;
      }
    }
    return {};
  }
};
// @lc code=end

/*
// @lcpr case=start
// [2,7,11,15]\n9\n
// @lcpr case=end

// @lcpr case=start
// [3,2,4]\n6\n
// @lcpr case=end

// @lcpr case=start
// [3,3]\n6\n
// @lcpr case=end

 */

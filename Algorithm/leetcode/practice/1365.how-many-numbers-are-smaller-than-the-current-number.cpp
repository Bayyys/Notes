/*
 * @lc app=leetcode.cn id=1365 lang=cpp
 * @lcpr version=30113
 *
 * [1365] 有多少小于当前数字的数字
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
  vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
    vector<int> sorted_nums = nums;
    sort(sorted_nums.begin(), sorted_nums.end());
    unordered_map<int, int> num2index;
    for (int i = nums.size() - 1; i >= 0; i--) {
      num2index[sorted_nums[i]] = i;
    }
    for (int i = 0; i < nums.size(); i++) {
      sorted_nums[i] = num2index[nums[i]];
    }
    return sorted_nums;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [8,1,2,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [6,5,4,8]\n
// @lcpr case=end

// @lcpr case=start
// [7,7,7,7]\n
// @lcpr case=end

 */

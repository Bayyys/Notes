/*
 * @lc app=leetcode.cn id=283 lang=cpp
 * @lcpr version=30110
 *
 * [283] 移动零
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
  void moveZeroes(vector<int>& nums) {
    int i = 0, j = 0;
    while (j < nums.size()) {
      if (nums[j] != 0) {
        nums[i] = nums[j];
        i++;
      }
      j++;
    }
    while (i < nums.size()) {
      nums[i] = 0;
      i++;
    }
  }
};
// @lc code=end

/*
// @lcpr case=start
// [0,1,0,3,12]\n
// @lcpr case=end

// @lcpr case=start
// [0]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=922 lang=cpp
 * @lcpr version=30113
 *
 * [922] 按奇偶排序数组 II
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
  vector<int> sortArrayByParityII(vector<int>& nums) {
    int length = nums.size();
    int even = 0, odd = 1;
    while (even < length && odd < length) {
      while (even < length && nums[even] % 2 == 0) even += 2;
      while (odd < length && nums[odd] % 2 == 1) odd += 2;
      if (even < length && odd < length) {
        swap(nums[even], nums[odd]);
        even += 2;
        odd += 2;
      }
    }
    return nums;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [4,2,5,7]\n
// @lcpr case=end

// @lcpr case=start
// [2,3]\n
// @lcpr case=end

 */

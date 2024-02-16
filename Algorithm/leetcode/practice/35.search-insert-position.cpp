/*
 * @lc app=leetcode.cn id=35 lang=cpp
 * @lcpr version=30113
 *
 * [35] 搜索插入位置
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
  int searchInsert(vector<int>& nums, int target) {
    int length = nums.size();
    if (nums[0] > target) return 0;
    if (nums[length - 1] < target) return length;
    int left = 0, right = length - 1;
    while (left <= right) {
      int mid = (left + right) / 2;
      if (nums[mid] == target)
        return mid;
      else if (nums[mid] > target)
        right = mid - 1;
      else if (nums[mid] < target)
        left = mid + 1;
    }
    return left;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,3,5,6]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,3,5,6]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,3,5,6]\n7\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=977 lang=cpp
 * @lcpr version=30110
 *
 * [977] 有序数组的平方
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
  vector<int> sortedSquares(vector<int>& nums) {
    vector<int> res(nums.size());
    int i = 0, j = nums.size() - 1;
    int k = nums.size() - 1;
    while (i <= j) {
      if (abs(nums[i]) > abs(nums[j])) {
        res[k--] = nums[i] * nums[i];
        i++;
      } else {
        res[k--] = nums[j] * nums[j];
        j--;
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [-4,-1,0,3,10]\n
// @lcpr case=end

// @lcpr case=start
// [-7,-3,2,3,11]\n
// @lcpr case=end

 */

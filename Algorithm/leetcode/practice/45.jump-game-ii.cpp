/*
 * @lc app=leetcode.cn id=45 lang=cpp
 * @lcpr version=30111
 *
 * [45] 跳跃游戏 II
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
  int jump(vector<int>& nums) {
    if (nums.size() == 1) return 0;
    int cur = 0, next = 0, step = 0;
    for (int i = 0; i < nums.size() - 1; i++) {
      next = max(next, i + nums[i]);
      if (i == cur) {
        step++;
        cur = next;
      }
    }
    return step;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [2,3,1,1,4]\n
// @lcpr case=end

// @lcpr case=start
// [2,3,0,1,4]\n
// @lcpr case=end

 */

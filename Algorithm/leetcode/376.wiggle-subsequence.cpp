/*
 * @lc app=leetcode.cn id=376 lang=cpp
 * @lcpr version=30111
 *
 * [376] 摆动序列
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
  int wiggleMaxLength(vector<int>& nums) {
    int res = 1;
    int pre = nums[0];
    int cur = 0;
    int flag = 0;  // 0: 平 1: 上 2: 下
    for (int i = 1; i < nums.size(); i++) {
      cur = nums[i];
      if (pre < cur) {
        if (flag == 0 || flag == 2) {
          res++;
          flag = 1;
        //   cout << "pre: " << pre << " cur: " << cur << endl;
        }
      } else if (pre > cur) {
        if (flag == 0 || flag == 1) {
          res++;
          flag = 2;
        //   cout << "pre: " << pre << " cur: " << cur << endl;
        }
      }
      pre = cur;
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,7,4,9,2,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,17,5,10,13,15,10,5,16,8]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9]\n
// @lcpr case=end

 */

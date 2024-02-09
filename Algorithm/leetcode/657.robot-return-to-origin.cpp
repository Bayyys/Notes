/*
 * @lc app=leetcode.cn id=657 lang=cpp
 * @lcpr version=30116
 *
 * [657] 机器人能否返回原点
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

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

// @lcpr-template-end
// @lc code=start
class Solution {
 public:
  bool judgeCircle(string moves) {
    int x = 0, y = 0;
    for (auto &c : moves) {
      if (c == 'U')
        y++;
      else if (c == 'D')
        y--;
      else if (c == 'L')
        x--;
      else if (c == 'R')
        x++;
    }
    if (x == 0 && y == 0) {
      return true;
    } else {
      return false;
    }
  }
};
// @lc code=end

/*
// @lcpr case=start
// "UD"\n
// @lcpr case=end

// @lcpr case=start
// "LL"\n
// @lcpr case=end

 */

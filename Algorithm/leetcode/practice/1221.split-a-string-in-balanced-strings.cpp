/*
 * @lc app=leetcode.cn id=1221 lang=cpp
 * @lcpr version=30116
 *
 * [1221] 分割平衡字符串
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
  int balancedStringSplit(string s) {
    int cnt = 0, ans = 0;
    char flag;
    for (auto &c : s) {
      if (cnt == 0) {
        flag = c;
        cnt = 1;
        ans++;
      } else if (c == flag)
        cnt++;
      else
        cnt--;
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "RLRRLLRLRL"\n
// @lcpr case=end

// @lcpr case=start
// "RLRRRLLRLL"\n
// @lcpr case=end

// @lcpr case=start
// "LLLLRRRR"\n
// @lcpr case=end

 */

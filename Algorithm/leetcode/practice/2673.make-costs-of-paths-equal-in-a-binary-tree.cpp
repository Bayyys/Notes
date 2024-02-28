/*
 * @lc app=leetcode.cn id=2673 lang=cpp
 * @lcpr version=30117
 *
 * [2673] 使二叉树所有路径值相等的最小代价
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
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

// struct ListNode {
//   int val;
//   ListNode *next;
//   ListNode() : val(0), next(nullptr) {}
//   ListNode(int x) : val(x), next(nullptr) {}
//   ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

// struct TreeNode {
//   int val;
//   TreeNode *left;
//   TreeNode *right;
//   TreeNode() : val(0), left(nullptr), right(nullptr) {}
//   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//   TreeNode(int x, TreeNode *left, TreeNode *right)
//       : val(x), left(left), right(right) {}
// };

// @lcpr-template-end
class Solution {
 public:
  int minIncrements(int n, vector<int> &cost) {
    int ans = 0;
    for (int i = n - 2; i > 0; i -= 2) {
      ans += abs(cost[i] - cost[i + 1]);
      cost[i / 2] += max(cost[i], cost[i + 1]);
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// 7\n[1,5,2,2,3,3,1]\n
// @lcpr case=end

// @lcpr case=start
// 3\n[5,3,3]\n
// @lcpr case=end

 */

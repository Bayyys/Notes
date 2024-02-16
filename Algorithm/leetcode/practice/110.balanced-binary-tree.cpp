/*
 * @lc app=leetcode.cn id=110 lang=cpp
 * @lcpr version=30110
 *
 * [110] 平衡二叉树
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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
 public:
  int getH(TreeNode* node) {
    queue<TreeNode*> q;
    if (node == nullptr)
      return 0;
    else
      q.push(node);
    int h = 0;
    while (!q.empty()) {
      int size = q.size();
      while (size--) {
        TreeNode* cur = q.front();
        q.pop();
        if (cur->left) q.push(cur->left);
        if (cur->right) q.push(cur->right);
      }
      h++;
    }
    return h;
  }
  bool isBalanced(TreeNode* root) {
    stack<TreeNode*> s;
    if (root) s.push(root);
    while (!s.empty()) {
      TreeNode* node = s.top();
      s.pop();
      if (abs(getH(node->left) - getH(node->right)) > 1)
        return false;
      else {
        if (node->left) s.push(node->left);
        if (node->right) s.push(node->right);
      }
    }
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,9,20,null,null,15,7]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,2,3,3,null,null,4,4]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

 */

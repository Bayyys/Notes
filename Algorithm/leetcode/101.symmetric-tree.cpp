/*
 * @lc app=leetcode.cn id=101 lang=cpp
 * @lcpr version=30110
 *
 * [101] 对称二叉树
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
  // 1. 递归
  bool isSymmetric1(TreeNode* root) {
    if (!root) return true;
    return cmp(root->left, root->right);
  }
  bool cmp(TreeNode* left, TreeNode* right) {
    if (!left && !right)
      return true;
    else if (!left || !right)
      return false;
    else if (left->val != right->val)
      return false;
    else
      return cmp(left->left, right->right) && cmp(left->right, right->left);
  }
  // 2. 迭代
  bool isSymmetric(TreeNode* root) {
    if (!root) return true;
    queue<TreeNode*> q;
    q.push(root->left);
    q.push(root->right);
    while (!q.empty()) {
      TreeNode* left = q.front();
      q.pop();
      TreeNode* right = q.front();
      q.pop();
      if (!left && !right)
        continue;
      else if (!left || !right)
        return false;
      else if (left->val != right->val)
        return false;
      q.push(left->left);
      q.push(right->right);
      q.push(left->right);
      q.push(right->left);
    }
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,2,3,4,4,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,2,null,3,null,3]\n
// @lcpr case=end

 */

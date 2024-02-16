/*
 * @lc app=leetcode.cn id=669 lang=cpp
 * @lcpr version=30111
 *
 * [669] 修剪二叉搜索树
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
  TreeNode* trimBST(TreeNode* root, int low, int high) {
    // if (!root) return root;
    // if (root->val < low) return trimBST(root->right, low, high);
    // if (root->val > high) return trimBST(root->left, low, high);
    // root->left = trimBST(root->left, low, high);
    // root->right = trimBST(root->right, low, high);
    // return root;
    if (!root) return root;
    // 处理头结点
    while (root && (root->val < low || root->val > high)) {
      if (root->val < low)
        root = root->right;
      else
        root = root->left;
    }
    TreeNode* cur = root;
    // 处理左孩子
    while (cur) {
      while (cur->left && cur->left->val < low) {  // 左孩子小于low
        cur->left = cur->left->right;  // 左孩子的右孩子上移
      }
      cur = cur->left;
    }
    cur = root;
    // 处理右孩子
    while (cur) {
      while (cur->right && cur->right->val > high) {
        cur->right = cur->right->left;
      }
      cur = cur->right;
    }
    return root;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,0,2]\n1\n2\n
// @lcpr case=end

// @lcpr case=start
// [3,0,4,null,2,null,null,1]\n1\n3\n
// @lcpr case=end

 */

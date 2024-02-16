/*
 * @lc app=leetcode.cn id=404 lang=cpp
 * @lcpr version=30111
 *
 * [404] 左叶子之和
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
  int sumOfLeftLeaves(TreeNode* root) {
    // 左叶子节点: 左子节点 && 左子节点没有子节点
    // 1. 递归法
    // if (!root)
    //   return 0;
    // else if (root->left && !root->left->left && !root->left->right) {
    //   // 左叶子节点的情况
    //   return root->left->val + sumOfLeftLeaves(root->right);
    // } else {
    //   // 非左叶子节点的情况
    //   return sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    // }

    // 2. 迭代法
    stack<TreeNode*> st;
    int res = 0;
    if (root) st.push(root);
    while (!st.empty()) {
      TreeNode* node = st.top();
      st.pop();
      if (node->left && !node->left->left && !node->left->right)
        res += node->left->val;
      if (node->left) st.push(node->left);
      if (node->right) st.push(node->right);
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,9,20,null,null,15,7]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

 */

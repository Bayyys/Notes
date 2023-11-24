/*
 * @lc app=leetcode.cn id=226 lang=cpp
 * @lcpr version=30110
 *
 * [226] 翻转二叉树
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
  TreeNode* invertTree(TreeNode* root) {
    // if (root == nullptr) return root;
    // swap(root->left, root->right);
    // invertTree(root->left);
    // invertTree(root->right);
    // return root;
    stack<TreeNode*> s;
    if (root) s.push(root);
    while (!s.empty()) {
      TreeNode* cur = s.top();
      s.pop();
      if (cur) {
        if (cur->right) s.push(cur->right);
        if (cur->left) s.push(cur->left);
        s.push(cur);
        s.push(nullptr);
      } else {
        cur = s.top();
        s.pop();
        swap(cur->left, cur->right);
      }
    }
    return root;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [4,2,7,1,3,6,9]\n
// @lcpr case=end

// @lcpr case=start
// [2,1,3]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

 */

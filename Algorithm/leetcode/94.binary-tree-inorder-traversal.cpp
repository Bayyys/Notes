/*
 * @lc app=leetcode.cn id=94 lang=cpp
 * @lcpr version=30110
 *
 * [94] 二叉树的中序遍历
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
  // void inorder(TreeNode* cur, vector<int>& vec) {
  //   if (cur == nullptr) return;
  //   inorder(cur->left, vec);
  //   vec.push_back(cur->val);
  //   inorder(cur->right, vec);
  // }

  vector<int> inorderTraversal(TreeNode* root) {
    vector<int> res;
    if (root == nullptr) return res;
    // inorder(root, res);
    stack<TreeNode*> st;
    TreeNode* cur = root;
    while (cur != nullptr || !st.empty()) {
      if (cur != nullptr) {
        st.push(cur);
        cur = cur->left;
      } else {
        TreeNode* node = st.top();
        st.pop();
        res.push_back(node->val);
        cur = node->right;
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,null,2,3]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

 */

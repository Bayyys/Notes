/*
 * @lc app=leetcode.cn id=222 lang=cpp
 * @lcpr version=30110
 *
 * [222] 完全二叉树的节点个数
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
  int countNodes(TreeNode* root) {
    stack<TreeNode*> st;
    if (root) st.push(root);
    int res = 0;
    while (!st.empty()) {
      TreeNode* node = st.top();
      st.pop();
      if (node) {
        if (node->left) st.push(node->left);
        if (node->right) st.push(node->right);
        st.push(node);
        st.push(nullptr);
      } else {
        node = st.top();
        st.pop();
        res++;
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3,4,5,6]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

 */

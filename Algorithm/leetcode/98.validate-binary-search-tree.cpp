/*
 * @lc app=leetcode.cn id=98 lang=cpp
 * @lcpr version=30111
 *
 * [98] 验证二叉搜索树
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
  //   TreeNode* pre; // 用于记录前一个节点(递归法)
  bool isValidBST(TreeNode* root) {
    // 使用中序遍历(左根右: 保证前一个节点比后一个节点小即可)
    // left < root < right
    // (注意是所有的左子树都小于根节点，所有的右子树都大于根节点)
    // 1. 递归
    // if (!root) return true;
    // bool left = isValidBST(root->left);
    // if (pre && pre->val >= root->val) return false;
    // pre = root;
    // bool right = isValidBST(root->right);
    // return left && right;
    // 2. 迭代
    stack<TreeNode*> st;
    TreeNode* cur = root;
    TreeNode* pre = nullptr;  // 用于记录前一个节点
    while (cur || !st.empty()) {
      if (cur) {
        st.push(cur);
        cur = cur->left;
      } else {
        cur = st.top();
        st.pop();
        if (pre && pre->val >= cur->val) return false;
        pre = cur;
        cur = cur->right;
      }
    }
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [2,1,3]\n
// @lcpr case=end

// @lcpr case=start
// [5,1,4,null,null,3,6]\n
// @lcpr case=end

 */

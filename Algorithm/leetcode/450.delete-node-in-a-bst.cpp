/*
 * @lc app=leetcode.cn id=450 lang=cpp
 * @lcpr version=30111
 *
 * [450] 删除二叉搜索树中的节点
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
  TreeNode* deleteNode(TreeNode* root, int key) {
    // if (!root) return root;  // 空节点
    // if (root->val == key) {
    //   if (!root->left && !root->right) {  // 左右孩子均为空节点
    //     delete root;
    //     return nullptr;
    //   } else if (!root->left) {  // 左孩子为空节点
    //     auto node = root->right;
    //     delete root;
    //     return node;
    //   } else if (!root->right) {  // 右孩子为空节点
    //     auto node = root->left;
    //     delete root;
    //     return node;
    //   } else {  // 左右孩子均不为空节点: 将左子树挂在右子树的最左节点上
    //     auto cur = root->right;
    //     while (cur->left) cur = cur->left;
    //     cur->left = root->left;
    //     auto tmp = root;
    //     root = root->right;
    //     delete tmp;
    //     return root;
    //   }
    // }
    // if (root->val > key) root->left = deleteNode(root->left, key);
    // if (root->val < key) root->right = deleteNode(root->right, key);
    // return root;

    /* 交换该节点和右子树最左侧节点的值, 此时该指定节点一定没有左子树,
     * 可以直接删除 */
    if (!root) return root;
    if (root->val == key) {
      if (!root->right) return root->left;
      auto cur = root->right;
      while (cur->left) cur = cur->left;
      swap(root->val, cur->val);
    }
    root->left = deleteNode(root->left, key);
    root->right = deleteNode(root->right, key);
    return root;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [5,3,6,2,4,null,7]\n3\n
// @lcpr case=end

// @lcpr case=start
// [5,3,6,2,4,null,7]\n0\n
// @lcpr case=end

// @lcpr case=start
// []\n0\n
// @lcpr case=end

 */

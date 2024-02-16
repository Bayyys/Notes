/*
 * @lc app=leetcode.cn id=106 lang=cpp
 * @lcpr version=30111
 *
 * [106] 从中序与后序遍历序列构造二叉树
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
  TreeNode* traversal(vector<int>& inorder, int in_left, int in_right,
                      vector<int>& postorder, int post_left, int post_right) {
    if (post_left == post_right) return nullptr;
    int node_val = postorder[post_right - 1];
    TreeNode* node = new TreeNode(node_val);
    if (post_left == post_right - 1) return node;  // 只有一个节点
    int delimiterIndex;
    for (delimiterIndex = in_left; delimiterIndex < in_right;
         delimiterIndex++) {
      if (inorder[delimiterIndex] == node_val) break;  // 找到中序遍历中的分界点
    }
    // 切割中序遍历数组
    int left_in_left = in_left;
    int left_in_right = delimiterIndex;
    int right_in_left = delimiterIndex + 1;
    int right_in_right = in_right;

    // 切割后序遍历数组
    int left_post_left = post_left;
    int left_post_right = post_left + (delimiterIndex - in_left);
    int right_post_left = post_left + (delimiterIndex - in_left);
    int right_post_right = post_right - 1;

    node->left = traversal(inorder, left_in_left, left_in_right, postorder,
                           left_post_left, left_post_right);
    node->right = traversal(inorder, right_in_left, right_in_right, postorder,
                            right_post_left, right_post_right);
    return node;
  }
  TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
    if (inorder.size() == 0 || postorder.size() == 0) return nullptr;
    return traversal(inorder, 0, inorder.size(), postorder, 0,
                     postorder.size());
  }
};
// @lc code=end

/*
// @lcpr case=start
// [9,3,15,20,7]\n[9,15,7,20,3]\n
// @lcpr case=end

// @lcpr case=start
// [-1]\n[-1]\n
// @lcpr case=end

 */

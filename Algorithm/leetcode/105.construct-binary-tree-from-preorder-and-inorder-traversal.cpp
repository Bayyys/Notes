/*
 * @lc app=leetcode.cn id=105 lang=cpp
 * @lcpr version=30111
 *
 * [105] 从前序与中序遍历序列构造二叉树
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
  TreeNode* TV(vector<int>& preorder, int pre_begin, int pre_end,
               vector<int>& inorder, int in_begin, int in_end) {
    // preorder: [pre_begin, pre_end)
    // inorder: [in_begin, in_end)
    if (pre_begin >= pre_end) return nullptr;
    int node_val = preorder[pre_begin];
    TreeNode* node = new TreeNode(node_val);
    if (pre_end == pre_begin + 1) return node;  // 只有一个节点
    int delimiterIndex;
    for (delimiterIndex = in_begin; delimiterIndex < in_end; delimiterIndex++) {
      if (inorder[delimiterIndex] == node_val) break;  // 找到中序遍历中的分界点
    }
    // inorder 分割:
    // [in_begin, delimiterIndex)
    // [delimiterIndex + 1, in_end)
    int left_in_begin = in_begin;
    int left_in_end = delimiterIndex;
    int right_in_begin = delimiterIndex + 1;
    int right_in_end = in_end;
    // preorder 分割:
    // [pre_begin + 1, pre_begin + 1 + (delimiterIndex - in_begin))
    // [pre_begin + 1 + (delimiterIndex - in_begin), pre_end)
    int left_pre_begin = pre_begin + 1;
    int left_pre_end = pre_begin + 1 + (delimiterIndex - in_begin);
    int right_pre_begin = pre_begin + 1 + (delimiterIndex - in_begin);
    int right_pre_end = pre_end;
    node->left = TV(preorder, left_pre_begin, left_pre_end, inorder,
                    left_in_begin, left_in_end);
    node->right = TV(preorder, right_pre_begin, right_pre_end, inorder,
                     right_in_begin, right_in_end);
    return node;
  }
  TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    if (preorder.size() == 0 || inorder.size() == 0) return nullptr;
    return TV(preorder, 0, preorder.size(), inorder, 0, inorder.size());
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,9,20,15,7]\n[9,3,15,20,7]\n
// @lcpr case=end

// @lcpr case=start
// [-1]\n[-1]\n
// @lcpr case=end

 */

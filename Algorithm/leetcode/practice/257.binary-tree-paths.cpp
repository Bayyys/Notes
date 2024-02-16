/*
 * @lc app=leetcode.cn id=257 lang=cpp
 * @lcpr version=30111
 *
 * [257] 二叉树的所有路径
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
  void preOrder(TreeNode* node, string path, vector<string>& res) {
    path += to_string(node->val);
    if (!node->left && !node->right) {
      // 叶子节点
      res.push_back(path);
      return;
    }
    if (node->left) preOrder(node->left, path + "->", res);
    if (node->right) preOrder(node->right, path + "->", res);
  }
  vector<string> binaryTreePaths(TreeNode* root) {
    // 前序遍历: 根左右
    // 递归终止条件: 当前节点的左右节点均为空
    vector<string> res;
    string path;
    if (!root) return res;
    preOrder(root, path, res);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3,null,5]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

 */

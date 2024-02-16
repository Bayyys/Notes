/*
 * @lc app=leetcode.cn id=513 lang=cpp
 * @lcpr version=30111
 *
 * [513] 找树左下角的值
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
  int maxDepth = INT_MIN;
  int res;
  void preOrder(TreeNode* node, int depth) {
    if (!node->left && !node->right) {
      // 叶子节点
      if (depth > maxDepth) {
        maxDepth = depth;
        res = node->val;
      }
      return;
    }
    if (node->left) preOrder(node->left, depth + 1);
    if (node->right) preOrder(node->right, depth + 1);
    return;
  }
  int findBottomLeftValue(TreeNode* root) {
    // 1. 递归法(前序遍历)
    if (!root) return 0;
    preOrder(root, 0);
    return res;

    // 2. 迭代法(层次遍历)
    // queue<TreeNode*> que;
    // if (root) que.push(root);
    // int res = 0;
    // while (!que.empty()) {
    //   int size = que.size();
    //   for (int i = 0; i < size; i++) {
    //     TreeNode* node = que.front();
    //     que.pop();
    //     if (0 == i) res = node->val;
    //     if (node->left) que.push(node->left);
    //     if (node->right) que.push(node->right);
    //   }
    // }
    // return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [2,1,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,null,5,6,null,null,7]\n
// @lcpr case=end

 */

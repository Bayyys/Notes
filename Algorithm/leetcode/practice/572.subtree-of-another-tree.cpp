/*
 * @lc app=leetcode.cn id=572 lang=cpp
 * @lcpr version=30111
 *
 * [572] 另一棵树的子树
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
  bool isSubtree(TreeNode* root, TreeNode* subRoot) {
    if (root == nullptr && subRoot == nullptr)
      return true;
    else if (root == nullptr)
      return false;
    else if (subRoot == nullptr)
      return true;
    else
      return isSameTree(root, subRoot) || isSubtree(root->left, subRoot) ||
             isSubtree(root->right, subRoot);
  }

  bool isSameTree(TreeNode* a, TreeNode* b) {
    if (a == nullptr && b == nullptr)
      return true;
    else if (a == nullptr || b == nullptr)
      return false;
    else if (a->val != b->val)
      return false;
    return isSameTree(a->left, b->left) && isSameTree(a->right, b->right);
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,4,5,1,2]\n[4,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,4,5,1,2,null,null,null,null,0]\n[4,1,2]\n
// @lcpr case=end

 */

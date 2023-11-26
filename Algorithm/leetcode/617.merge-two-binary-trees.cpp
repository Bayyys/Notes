/*
 * @lc app=leetcode.cn id=617 lang=cpp
 * @lcpr version=30111
 *
 * [617] 合并二叉树
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
  TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
    if (root1 == nullptr && root2 == nullptr) return nullptr;
    if (root1 == nullptr) return root2;
    if (root2 == nullptr) return root1;
    TreeNode* root = new TreeNode(root1->val + root2->val);
    root->left = mergeTrees(root1->left, root2->left);
    root->right = mergeTrees(root1->right, root2->right);
    return root;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,3,2,5]\n[2,1,3,null,4,null,7]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n[1,2]\n
// @lcpr case=end

 */

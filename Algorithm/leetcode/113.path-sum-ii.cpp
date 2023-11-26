/*
 * @lc app=leetcode.cn id=113 lang=cpp
 * @lcpr version=30111
 *
 * [113] 路径总和 II
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
  void dfs(TreeNode* root, int targetSum, vector<int>& path,
           vector<vector<int>>& res) {
    if (!root->left && !root->right) {
      if (targetSum == 0) res.push_back(path);
      return;
    }
    if (root->left) {
      path.push_back(root->left->val);
      dfs(root->left, targetSum - root->left->val, path, res);
      path.pop_back();
    }
    if (root->right) {
      path.push_back(root->right->val);
      dfs(root->right, targetSum - root->right->val, path, res);
      path.pop_back();
    }
  }

  vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
    vector<vector<int>> res;
    vector<int> path;
    if (!root) return res;
    path.push_back(root->val);
    dfs(root, targetSum - root->val, path, res);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n0\n
// @lcpr case=end

 */

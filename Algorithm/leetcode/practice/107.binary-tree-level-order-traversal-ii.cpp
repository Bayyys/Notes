/*
 * @lc app=leetcode.cn id=107 lang=cpp
 * @lcpr version=30110
 *
 * [107] 二叉树的层序遍历 II
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
  //   void order(TreeNode* root, vector<vector<int>>& res, int depth) {
  //     if (!root) return;
  //     if (res.size() == depth) res.push_back(vector<int>());
  //     res[depth].push_back(root->val);
  //     order(root->left, res, depth + 1);
  //     order(root->right, res, depth + 1);
  //   }

  vector<vector<int>> levelOrderBottom(TreeNode* root) {
    vector<vector<int>> res;
    queue<TreeNode*> q;
    if (root) q.push(root);
    while (!q.empty()) {
      int size = q.size();
      vector<int> vec;
      for (int i = 0; i < size; i++) {
        TreeNode* cur = q.front();
        q.pop();
        vec.push_back(cur->val);
        if (cur->left) q.push(cur->left);
        if (cur->right) q.push(cur->right);
      }
      res.push_back(vec);
    }
    reverse(res.begin(), res.end());
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,9,20,null,null,15,7]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

 */

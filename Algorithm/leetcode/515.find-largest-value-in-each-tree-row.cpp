/*
 * @lc app=leetcode.cn id=515 lang=cpp
 * @lcpr version=30110
 *
 * [515] 在每个树行中找最大值
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
  vector<int> largestValues(TreeNode* root) {
    vector<int> res;
    queue<TreeNode*> q;
    if (root != nullptr) q.push(root);
    while (!q.empty()) {
      int size = q.size();
      int max = INT32_MIN;
      for (int i = 0; i < size; i++) {
        TreeNode* node = q.front();
        q.pop();
        if (node->val > max) max = node->val;
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
      }
      res.push_back(max);
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,3,2,5,3,null,9]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

 */

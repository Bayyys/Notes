/*
 * @lc app=leetcode.cn id=337 lang=cpp
 * @lcpr version=30112
 *
 * [337] 打家劫舍 III
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
  int rob(TreeNode* root) {
    vector<int> res = rob_helper(root);
    return max(res[0], res[1]);
  }
  vector<int> rob_helper(TreeNode* root) {
    if (!root) return {0, 0};
    vector<int> left = rob_helper(root->left);
    vector<int> right = rob_helper(root->right);
    int val1 = root->val + left[0] + right[0];
    int val2 = max(left[0], left[1]) + max(right[0], right[1]);
    return {val2, val1};
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,2,3,null,3,null,1]\n
// @lcpr case=end

// @lcpr case=start
// [3,4,5,1,3,null,1]\n
// @lcpr case=end

 */

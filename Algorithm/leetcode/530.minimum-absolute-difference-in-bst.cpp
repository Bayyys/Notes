/*
 * @lc app=leetcode.cn id=530 lang=cpp
 * @lcpr version=30111
 *
 * [530] 二叉搜索树的最小绝对差
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
  int ans = INT_MAX;
  TreeNode* pre = nullptr;
  void TV(TreeNode* cur) {
    if (!cur) return;
    TV(cur->left);
    if (pre) ans = min(ans, cur->val - pre->val);
    pre = cur;
    TV(cur->right);
  }

  int getMinimumDifference(TreeNode* root) {
    // 1. 递归法
    // TV(root);

    // 2. 迭代法
    stack<TreeNode*> st;
    TreeNode* cur = root;
    TreeNode* pre = nullptr;
    while (cur || !st.empty()) {
      if (cur) {
        st.push(cur);
        cur = cur->left;
      } else {
        cur = st.top();
        st.pop();
        if (pre) ans = min(ans, cur->val - pre->val);
        pre = cur;
        cur = cur->right;
      }
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [4,2,6,1,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,0,48,null,null,12,49]\n
// @lcpr case=end

 */

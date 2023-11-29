/*
 * @lc app=leetcode.cn id=538 lang=cpp
 * @lcpr version=30111
 *
 * [538] 把二叉搜索树转换为累加树
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
  TreeNode* convertBST(TreeNode* root) {
    int pre = 0;

    stack<TreeNode*> st;
    TreeNode* cur = root;
    while (cur || !st.empty()) {
      if (cur) {
        st.push(cur);
        cur = cur->right;
      } else {
        cur = st.top();
        st.pop();
        cur->val += pre;
        pre = cur->val;
        cur = cur->left;
      }
    }
    return root;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\n
// @lcpr case=end

// @lcpr case=start
// [0,null,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,0,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,2,4,1]\n
// @lcpr case=end

 */

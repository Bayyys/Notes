/*
 * @lc app=leetcode.cn id=501 lang=cpp
 * @lcpr version=30111
 *
 * [501] 二叉搜索树中的众数
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
  vector<int> ans;  // 结果集
  int maxCnt = 0;   // 最大出现次数
  int count = 0;
  TreeNode* pre = nullptr;  // 前一个节点
  void TV(TreeNode* cur) {
    if (!cur) return;
    TV(cur->left);
    if (!pre) {
      count = 1;
    } else if (pre->val == cur->val) {
      count++;
    } else {
      count = 1;
    }
    pre = cur;
    if (count == maxCnt) {
      ans.push_back(cur->val);
    } else if (count > maxCnt) {
      maxCnt = count;
      ans.clear();
      ans.push_back(cur->val);
    }
    TV(cur->right);
    return;
  }
  vector<int> findMode(TreeNode* root) {
    // 1. 递归法
    // TV(root);

    // 2. 迭代法
    stack<TreeNode*> st;
    TreeNode* cur = root;
    while (cur || !st.empty()) {
      if (cur) {
        st.push(cur);
        cur = cur->left;
      } else {
        cur = st.top();
        st.pop();
        if (!pre) {
          count = 1;
        } else if (pre->val == cur->val) {
          count++;
        } else {
          count = 1;
        }
        pre = cur;
        if (count == maxCnt) {
          ans.push_back(cur->val);
        } else if (count > maxCnt) {
          maxCnt = count;
          ans.clear();
          ans.push_back(cur->val);
        }
        cur = cur->right;
      }
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,null,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [0]\n
// @lcpr case=end

 */

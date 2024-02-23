/*
 * @lc app=leetcode.cn id=2476 lang=cpp
 * @lcpr version=30117
 *
 * [2476] 二叉搜索树最近节点查询
 */

// @lcpr-template-start
#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <queue>
#include <set>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

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
 private:
  int n = 0;
  vector<int> nodes;
  vector<vector<int>> ans;  // 答案

  void InOrder(TreeNode *root) {
    if (root == nullptr) return;
    InOrder(root->left);
    nodes.emplace_back(root->val);
    InOrder(root->right);
  }

 public:
  vector<vector<int>> closestNodes(TreeNode *root, vector<int> &queries) {
    n = queries.size();
    InOrder(root);  // 中序遍历
    for (auto &q : queries) {
      int minVal = -1, maxVal = -1;
      auto it = lower_bound(nodes.begin(), nodes.end(),
                            q);  // 找到大于等于q的第一个元素
      if (it != nodes.end()) {
        maxVal = *it;
        if (*it == q) {
          minVal = maxVal;
          ans.push_back({minVal, maxVal});
          continue;
        }
      }
      if (it != nodes.begin()) {
        minVal = *(--it);
      }
      ans.push_back({minVal, maxVal});
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [6,2,13,1,4,9,15,null,null,null,null,null,null,14]\n[2,5,16]\n
// @lcpr case=end

// @lcpr case=start
// [4,null,9]\n[3]\n
// @lcpr case=end

 */

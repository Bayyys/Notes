/*
 * @lc app=leetcode.cn id=938 lang=cpp
 * @lcpr version=30117
 *
 * [938] 二叉搜索树的范围和
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
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

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
  int ans = 0;
  void dfs(TreeNode *root, int &low, int &high) {
    if (root == nullptr) {
      return;
    }
    if (root->val >= low && root->val <= high) {
      ans += root->val;
      dfs(root->left, low, high);
      dfs(root->right, low, high);
    } else if (root->val < low) {
      dfs(root->right, low, high);
    } else {
      dfs(root->left, low, high);
    }
  }

 public:
  int rangeSumBST(TreeNode *root, int low, int high) {
    dfs(root, low, high);
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [10,5,15,3,7,null,18]\n7\n15\n
// @lcpr case=end

// @lcpr case=start
// [10,5,15,3,7,13,18,1,null,6]\n6\n10\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=987 lang=cpp
 * @lcpr version=30116
 *
 * [987] 二叉树的垂序遍历
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
  vector<vector<int>> res;
  vector<vector<int>> res_left =
      vector<vector<int>>(1, vector<int>(1, 0));  // 左侧子树
  vector<vector<int>> res_right;                  // 右侧子树
  void TV(TreeNode *root, int row, int col) {
    if (!root) return;
    if (col < 0) {
      if (res_left.size() < -col + 1) res_left.push_back(vector<int>());
      res_left[-col].push_back(root->val);
    } else {
      if (res_right.size() < col + 1) res_right.push_back(vector<int>());
      res_right[col].push_back(root->val);
    }
    TV(root->left, row + 1, col - 1);
    TV(root->right, row + 1, col + 1);
  }

 public:
  vector<vector<int>> verticalTraversal(TreeNode *root) {
    if (!root) return {{}};
    if (!root->left && !root->right) return {{root->val}};
    TV(root, 0, 0);
    reverse(res_left.begin(), res_left.end());
    res = res_left;
    res.erase(res.begin() + res.size() - 1);
    res.insert(res_right.begin(), res_right.end() - 1, res_right.end());
    for (int i = 0; i < res_left.size(); i++) {
      for (auto j : res_left[i]) {
        cout << j << " ";
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,9,20,null,null,15,7]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,6,5,7]\n
// @lcpr case=end

 */

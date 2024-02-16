/*
 * @lc app=leetcode.cn id=968 lang=cpp
 * @lcpr version=30112
 *
 * [968] 监控二叉树
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
 private:
  int res;
  int TV(TreeNode* cur) {
    /**
     * @brief 0: 未被覆盖 1: 放置摄像头 2: 本节点有覆盖
     *
     */
    if (!cur) return 2;
    int left = TV(cur->left);
    int right = TV(cur->right);
    if (left == 2 && right == 2)
      return 0;                          // 本节点未被覆盖
    else if (left == 0 || right == 0) {  // 本节点未被覆盖
      res++;
      return 1;
    } else
      return 2;  // 本节点有覆盖(左右子节点有一个有覆盖
  }

 public:
  int minCameraCover(TreeNode* root) {
    if (TV(root) == 0) {
      res++;
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [0,0,null,0,0]\n
// @lcpr case=end

// @lcpr case=start
// [0,0,null,0,null,0,null,null,0]\n
// @lcpr case=end

 */

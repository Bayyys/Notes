/*
 * @lc app=leetcode.cn id=654 lang=cpp
 * @lcpr version=30111
 *
 * [654] 最大二叉树
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
  TreeNode* TV(vector<int>& nums, int begin, int end) {
    if (begin >= end) return nullptr;
    // 寻找最大值
    int max_index = begin;
    for (int i = begin + 1; i < end; i++) {
      if (nums[i] > nums[max_index]) max_index = i;
    }
    TreeNode* node = new TreeNode(nums[max_index]);
    // left [begin, max_index)
    node->left = TV(nums, begin, max_index);
    // right [max_index + 1, end)
    node->right = TV(nums, max_index + 1, end);

    return node;
  }
  TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
    return TV(nums, 0, nums.size());
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,2,1,6,0,5]\n
// @lcpr case=end

// @lcpr case=start
// [3,2,1]\n
// @lcpr case=end

 */

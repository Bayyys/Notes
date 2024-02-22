/*
 * @lc app=leetcode.cn id=889 lang=cpp
 * @lcpr version=30117
 *
 * [889] 根据前序和后序遍历构造二叉树
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
  TreeNode *TV(vector<int> &preorder, int pre_begin, int pre_end,
               vector<int> &postorder, int post_begin, int post_end) {
    // preorder: [pre_begin, pre_end]
    // postorder: [post_begin, post_end]

    // 空节点判断
    if (pre_begin > pre_end || post_begin > post_end) return nullptr;

    // 构建根节点
    int node_val = preorder[pre_begin];
    TreeNode *node = new TreeNode(node_val);
    if (pre_begin == pre_end) return node;  // 只有一个节点的情况(递归终止条件)

    // 左右节点
    int left_node_val = preorder[pre_begin + 1];

    // 找到前序遍历的分割点
    int idx = -1;
    for (idx = post_begin; idx <= post_end; idx++) {
      if (left_node_val == postorder[idx]) break;
    }
    node->left = TV(preorder, pre_begin + 1, pre_begin + 1 + (idx - post_begin),
                    postorder, post_begin, idx);
    node->right = TV(preorder, pre_begin + 1 + (idx - post_begin) + 1, pre_end,
                     postorder, idx + 1, post_end - 1);
    return node;
  }

 public:
  TreeNode *constructFromPrePost(vector<int> &preorder,
                                 vector<int> &postorder) {
    if (preorder.size() == 0) return nullptr;
    if (preorder.size() == 1) return new TreeNode(preorder[0]);
    int n = preorder.size();
    return TV(preorder, 0, n - 1, postorder, 0, n - 1);
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n[1]\n
// @lcpr case=end

 */

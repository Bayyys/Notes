/*
 * @lc app=leetcode.cn id=2917 lang=cpp
 * @lcpr version=30118
 *
 * [2917] 找出数组中的 K-or 值
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
class Solution {
 public:
  int findKOr(vector<int> &nums, int k) {
    int ans = 0;
    int n = nums.size();
    for (int i = 0; i < 31; i++) {
      int cnt = 0;
      for (auto num : nums) {
        if ((num >> i) & 1) {
          cnt++;
        }
      }
      if (cnt >= k) {
        ans |= (1 << i);
      }
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [7,12,9,8,9,15]\n4\n
// @lcpr case=end

// @lcpr case=start
// [2,12,1,11,4,5]\n6\n
// @lcpr case=end

// @lcpr case=start
// [10,8,5,9,11,6,8]\n1\n
// @lcpr case=end

 */

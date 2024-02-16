/*
 * @lc app=leetcode.cn id=132 lang=cpp
 * @lcpr version=30116
 *
 * [132] 分割回文串 II
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
class Solution {
 public:
  int minCut(string s) {
    vector<vector<bool>> isPalindromic(s.size(), vector<bool>(s.size(), false));
    for (int i = s.size() - 1; i >= 0; i--) {
      for (int j = i; j < s.size(); j++) {
        if (s[i] == s[j] && (j - i <= 1 || isPalindromic[i + 1][j - 1])) {
          isPalindromic[i][j] = true;
        }
      }
    }
    // 初始化
    vector<int> dp(s.size(), 0);
    for (int i = 0; i < s.size(); i++) dp[i] = i;

    for (int i = 1; i < s.size(); i++) {
      if (isPalindromic[0][i]) {
        dp[i] = 0;
        continue;
      }
      for (int j = 0; j < i; j++) {
        if (isPalindromic[j + 1][i]) {
          dp[i] = min(dp[i], dp[j] + 1);
        }
      }
    }
    return dp[s.size() - 1];
  }
};
// @lc code=end

/*
// @lcpr case=start
// "aab"\n
// @lcpr case=end

// @lcpr case=start
// "a"\n
// @lcpr case=end

// @lcpr case=start
// "ab"\n
// @lcpr case=end

 */

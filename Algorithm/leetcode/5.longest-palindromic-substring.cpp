/*
 * @lc app=leetcode.cn id=5 lang=cpp
 * @lcpr version=30116
 *
 * [5] 最长回文子串
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
  string longestPalindrome(string s) {
    vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), false));
    int left = 0, right = 0;
    int max_len = 0;
    for (int i = s.size() - 1; i >= 0; i--) {
      for (int j = i; j < s.size(); j++) {
        if (s[i] == s[j]) {
          if (j - i < 2 || dp[i + 1][j - 1]) {
            dp[i][j] = true;
            if (j - i + 1 > max_len) {
              max_len = j - i + 1;
              left = i;
              right = j;
            }
          }
        }
      }
    }
    return s.substr(left, right - left + 1);
  }
};
// @lc code=end

/*
// @lcpr case=start
// "babad"\n
// @lcpr case=end

// @lcpr case=start
// "cbbd"\n
// @lcpr case=end

 */

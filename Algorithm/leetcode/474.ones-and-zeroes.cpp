/*
 * @lc app=leetcode.cn id=474 lang=cpp
 * @lcpr version=30112
 *
 * [474] 一和零
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
class Solution {
 public:
  int findMaxForm(vector<string>& strs, int m, int n) {
    // m:0 n:1
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (string str : strs) {
      int zeros = 0, ones = 0;
      for (char c : str) {
        if (c == '0')
          zeros++;
        else
          ones++;
      }
      for (int i = m; i >= zeros; i--) {
        for (int j = n; j >= ones; j--) {
          dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);
        }
      }
    }
    return dp[m][n];
  }
};
// @lc code=end

/*
// @lcpr case=start
// ["10", "0001", "111001", "1", "0"]\n5\n3\n
// @lcpr case=end

// @lcpr case=start
// ["10", "0", "1"]\n1\n1\n
// @lcpr case=end

 */

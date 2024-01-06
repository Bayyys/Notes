/*
 * @lc app=leetcode.cn id=72 lang=cpp
 * @lcpr version=30112
 *
 * [72] 编辑距离
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
  int minDistance(string word1, string word2) {
    // dp[i][j]: 以i-1为结尾的word1子串和以j-1为结尾的word2子串的最小编辑距离
    // word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]    // 不需要编辑
    // word1[i-1] != word2[j-1]: dp[i][j] = min(dp[i-1][j], dp[i][j-1],
    // dp[i-1][j-1]) + 1
    // 1. 删除word1[i-1];
    // 2. 删除word2[j-1];
    // 3. 替换word1[i-1]为word2[j-1]
    vector<vector<int>> dp(word1.size() + 1, vector<int>(word2.size() + 1, 0));
    for (int i = 0; i <= word1.size(); i++) dp[i][0] = i;
    for (int j = 0; j <= word2.size(); j++) dp[0][j] = j;
    for (int i = 1; i <= word1.size(); i++) {
      for (int j = 1; j <= word2.size(); j++) {
        if (word1[i - 1] == word2[j - 1])
          dp[i][j] = dp[i - 1][j - 1];
        else
          dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
      }
    }
    return dp[word1.size()][word2.size()];
  }
};
// @lc code=end

/*
// @lcpr case=start
// "horse"\n"ros"\n
// @lcpr case=end

// @lcpr case=start
// "intention"\n"execution"\n
// @lcpr case=end

 */

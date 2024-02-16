/*
 * @lc app=leetcode.cn id=115 lang=cpp
 * @lcpr version=30112
 *
 * [115] 不同的子序列
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
  int numDistinct(string s, string t) {
    // dp[i][j]: 以i-1为结尾的s子串中，以j-1为结尾的t子串的个数
    //   0 b a g
    // 0 1 0 0 0
    // b 1 1 0 0
    // a 1 1 1 0
    // g 1 1 1 1
    // g 1 1 1 2
    vector<vector<uint64_t>> dp(s.size() + 1,
                                vector<uint64_t>(t.size() + 1, 0));
    for (int i = 0; i <= s.size(); i++) dp[i][0] = 1;
    for (int i = 1; i <= s.size(); i++) {
      for (int j = 1; j <= t.size(); j++) {
        if (s[i - 1] == t[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
        } else {
          dp[i][j] = dp[i - 1][j];
        }
      }
    }
    return dp[s.size()][t.size()];
  }
};
// @lc code=end

/*
// @lcpr case=start
// "rabbbit"\n"rabbit"\n
// @lcpr case=end

// @lcpr case=start
// "babgbag"\n"bag"\n
// @lcpr case=end

 */

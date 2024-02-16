/*
 * @lc app=leetcode.cn id=509 lang=cpp
 * @lcpr version=30112
 *
 * [509] 斐波那契数
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
  int fib(int n) {
    /**
     * 1. 确定dp数组以及下标的含义: dp[i]表示第i个斐波那契数
     * 2. 确定递推公式: dp[i] = dp[i-1] + dp[i-2]
     * 3. dp数组如何初始化: dp[0] = 0, dp[1] = 1
     * 4. 确定遍历顺序: 从前往后遍历
     * 5. 举例推导dp数组: 0 1 1 2 3 5 8 13 21 34
     */
    if (n <= 1) return n;
    int dp_2 = 0;
    int dp_1 = 1;
    int res = 0;
    for (int i = 2; i <= n; i++) {
      int temp = dp_2 + dp_1;
      dp_2 = dp_1;
      dp_1 = temp;
    }
    return dp_1;
  }
};
// @lc code=end

/*
// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 4\n
// @lcpr case=end

 */

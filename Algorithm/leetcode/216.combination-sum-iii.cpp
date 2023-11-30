/*
 * @lc app=leetcode.cn id=216 lang=cpp
 * @lcpr version=30111
 *
 * [216] 组合总和 III
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
  vector<vector<int>> res;
  vector<int> path;
  void TV(int goalSum, int k, int sum, int startIndex) {
    if (k == path.size()) {
      if (sum == goalSum) res.push_back(path);
      return;
    }
    for (int i = startIndex; i <= 9 - (k - path.size()) + 1; i++) {
      if (sum + i > goalSum) return;
      path.push_back(i);
      TV(goalSum, k, sum + i, i + 1);
      path.pop_back();
    }
  }
  vector<vector<int>> combinationSum3(int k, int n) {
    TV(n, k, 0, 1);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// 3\n7\n
// @lcpr case=end

// @lcpr case=start
// 3\n9\n
// @lcpr case=end

// @lcpr case=start
// 4\n1\n
// @lcpr case=end

 */

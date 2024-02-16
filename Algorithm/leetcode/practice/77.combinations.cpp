/*
 * @lc app=leetcode.cn id=77 lang=cpp
 * @lcpr version=30111
 *
 * [77] 组合
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
  void TV(int n, int k, int startIndex) {
    if (k == path.size()) {
      res.push_back(path);
      return;
    }
    for (int i = startIndex; i <= n - (k - path.size()) + 1; i++) {
      path.push_back(i);
      TV(n, k, i + 1);
      path.pop_back();
    }
  }
  vector<vector<int>> combine(int n, int k) {
    TV(n, k, 1);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// 4\n2\n
// @lcpr case=end

// @lcpr case=start
// 1\n1\n
// @lcpr case=end

 */

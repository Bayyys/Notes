/*
 * @lc app=leetcode.cn id=56 lang=cpp
 * @lcpr version=30112
 *
 * [56] 合并区间
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
  vector<vector<int>> merge(vector<vector<int>>& intervals) {
    vector<vector<int>> res;
    sort(intervals.begin(), intervals.end(),
         [](const auto& a, const auto& b) { return a[0] < b[0]; });
    res.push_back(intervals[0]);
    for (int i = 0; i < intervals.size(); i++) {
      if (res.back()[1] >= intervals[i][0]) {
        res.back()[1] = max(res.back()[1], intervals[i][1]);
      } else {
        res.push_back(intervals[i]);
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[1,3],[2,6],[8,10],[15,18]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,4],[4,5]]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=435 lang=cpp
 * @lcpr version=30112
 *
 * [435] 无重叠区间
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
  int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end(),
         [](const auto& a, const auto& b) { return a[1] < b[1]; });
    int count = 1;
    int end = intervals[0][1];
    for (int i = 1; i < intervals.size(); i++) {
      if (intervals[i][0] >= end) {
        count++;
        end = intervals[i][1];
      }
    }
    return intervals.size() - count;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[1,2],[2,3],[3,4],[1,3]]\n
// @lcpr case=end

// @lcpr case=start
// [ [1,2], [1,2], [1,2] ]\n
// @lcpr case=end

// @lcpr case=start
// [ [1,2], [2,3] ]\n
// @lcpr case=end

 */

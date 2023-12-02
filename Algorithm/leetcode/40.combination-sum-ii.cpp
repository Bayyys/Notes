/*
 * @lc app=leetcode.cn id=40 lang=cpp
 * @lcpr version=30111
 *
 * [40] 组合总和 II
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
  void TV(int startIndex, int target, vector<int>& candidates) {
    if (target <= 0) {
      if (target == 0) {
        res.push_back(path);
      }
      return;
    }
    for (int i = startIndex; i < candidates.size(); i++) {
      if (i > startIndex && candidates[i] == candidates[i - 1]) continue;
      if (target - candidates[i] < 0) break;
      path.push_back(candidates[i]);
      TV(i + 1, target - candidates[i], candidates);
      path.pop_back();
    }
  }
  vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    TV(0, target, candidates);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [10,1,2,7,6,1,5]\n8,\n
// @lcpr case=end

// @lcpr case=start
// [2,5,2,1,2]\n5,\n
// @lcpr case=end

 */

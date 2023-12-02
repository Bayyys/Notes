/*
 * @lc app=leetcode.cn id=39 lang=cpp
 * @lcpr version=30111
 *
 * [39] 组合总和
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
  void TV(int i, int target, int sum, vector<int>& candidates) {
    if (target <= 0) {
      if (target == 0) {
        res.push_back(path);
      }
      return;
    }
    for (; i < candidates.size(); i++) {
      if (sum + candidates[i] > target) break;
      path.push_back(candidates[i]);
      TV(i, target - candidates[i], sum, candidates);
      path.pop_back();
    }
  }
  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    TV(0, target, 0, candidates);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [2,3,6,7]\n7\n
// @lcpr case=end

// @lcpr case=start
// [2,3,5]\n8\n
// @lcpr case=end

// @lcpr case=start
// [2]\n1\n
// @lcpr case=end

 */

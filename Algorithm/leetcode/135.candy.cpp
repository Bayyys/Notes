/*
 * @lc app=leetcode.cn id=135 lang=cpp
 * @lcpr version=30112
 *
 * [135] 分发糖果
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
  int candy(vector<int>& ratings) {
    vector<int> candy(ratings.size(), 1);
    for (int i = 1; i < ratings.size(); i++) {
      if (ratings[i] > ratings[i - 1]) candy[i] = candy[i - 1] + 1;
    }
    for (int i = ratings.size() - 2; i >= 0; i--) {
      if (ratings[i] > ratings[i + 1])
        candy[i] = max(candy[i], candy[i + 1] + 1);
    }
    int res = 0;
    for (auto i : candy) {
      res += i;
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,0,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,2]\n
// @lcpr case=end

 */

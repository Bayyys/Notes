/*
 * @lc app=leetcode.cn id=1207 lang=cpp
 * @lcpr version=30113
 *
 * [1207] 独一无二的出现次数
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
  bool uniqueOccurrences(vector<int>& arr) {
    unordered_map<int, int> cnts;
    for (auto num : arr) {
      if (cnts.find(num) == cnts.end())
        cnts[num] = 1;
      else
        cnts[num]++;
    }
    unordered_map<int, int> cnts_cnts;
    for (auto cnt : cnts) {
      if (cnts_cnts.find(cnt.second) == cnts_cnts.end())
        cnts_cnts[cnt.second] = 1;
      else
        return false;
    }
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,2,1,1,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n
// @lcpr case=end

// @lcpr case=start
// [-3,0,1,-3,1,1,1,-3,10,0]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=738 lang=cpp
 * @lcpr version=30112
 *
 * [738] 单调递增的数字
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
  int monotoneIncreasingDigits(int n) {
    string s = to_string(n);
    for (int i = s.size() - 1; i > 0; i--) {
      if (s[i] < s[i - 1]) {
        s[i - 1]--;
        for (int j = i; j < s.size(); j++) {
          s[j] = '9';
        }
      }
    }
    return stoi(s);
  }
};
// @lc code=end

/*
// @lcpr case=start
// 10\n
// @lcpr case=end

// @lcpr case=start
// 1234\n
// @lcpr case=end

// @lcpr case=start
// 332\n
// @lcpr case=end

 */

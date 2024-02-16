/*
 * @lc app=leetcode.cn id=17 lang=cpp
 * @lcpr version=30111
 *
 * [17] 电话号码的字母组合
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
  const vector<string> table = {"",    "",    "abc",  "def", "ghi",
                                "jkl", "mno", "pqrs", "tuv", "wxyz"};
  vector<string> res;
  void TV(const string& digits, int index, const string& path) {
    if (index == digits.size()) {
      res.push_back(path);
      return;
    }
    int digit = digits[index] - '0';
    string str = table[digit];
    for (int i = 0; i < str.size(); i++) {
      TV(digits, index + 1, path + str[i]);
    }
  }
  vector<string> letterCombinations(string digits) {
    if (digits.empty()) return res;
    TV(digits, 0, "");
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "23"\n
// @lcpr case=end

// @lcpr case=start
// ""\n
// @lcpr case=end

// @lcpr case=start
// "2"\n
// @lcpr case=end

 */

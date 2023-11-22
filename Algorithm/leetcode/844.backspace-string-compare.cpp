/*
 * @lc app=leetcode.cn id=844 lang=cpp
 * @lcpr version=30110
 *
 * [844] 比较含退格的字符串
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
  bool backspaceCompare(string s, string t) {
    return getDeleteBack(s).compare(getDeleteBack(t)) == 0;
  }
  string getDeleteBack(string& s) {
    int i = 0, j = 0;
    int count = 0;
    while (j < s.size()) {
      if (s[j] != '#') {
        s[i] = s[j];
        i++;
      } else {
        if (i != 0) {
          i--;
        }
      }
      j++;
    }
    return s.substr(0, i);
  }
};
// @lc code=end

/*
// @lcpr case=start
// "ab#c"\n"ad#c"\n
// @lcpr case=end

// @lcpr case=start
// "ab##"\n"c#d#"\n
// @lcpr case=end

// @lcpr case=start
// "a#c"\n"b"\n
// @lcpr case=end

 */

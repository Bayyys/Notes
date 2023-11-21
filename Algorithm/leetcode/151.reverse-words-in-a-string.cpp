/*
 * @lc app=leetcode.cn id=151 lang=cpp
 * @lcpr version=30110
 *
 * [151] 反转字符串中的单词
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
  string reverseWords(string s) {
    // 1. 去除多余空格
    int slow = 0;
    int w_begin = 0, w_end = 0;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] != ' ') {
        if (slow != 0) s[slow++] = ' ';
        while (i < s.size() && s[i] != ' ') s[slow++] = s[i++];
      }
    }
    s.resize(slow);

    // 2. 反转整个字符串
    reverse(s.begin(), s.end());

    // 3. 反转每个单词
    for (int i = 0; i < s.size(); i++) {
      if (s[i] != ' ') {
        w_begin = i;
        while (i < s.size() && s[i] != ' ') i++;
        w_end = i - 1;
        reverse(s.begin() + w_begin, s.begin() + w_end + 1);
      }
    }
    return s;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "the sky is blue"\n
// @lcpr case=end

// @lcpr case=start
// "  hello world  "\n
// @lcpr case=end

// @lcpr case=start
// "a good   example"\n
// @lcpr case=end

 */

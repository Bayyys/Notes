/*
 * @lc app=leetcode.cn id=344 lang=cpp
 * @lcpr version=30110
 *
 * [344] 反转字符串
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
  void reverseString(vector<char>& s) {
    for (int i = 0, j = s.size() - 1; i < j; i++, j--) {
      mySwap2(s[i], s[j]);
    }
  }

  void mySwap(char& a, char& b) {
    char tmp = a;
    a = b;
    b = tmp;
  }

  void mySwap2(char& a, char& b) {
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
  }
};
// @lc code=end

/*
// @lcpr case=start
// ["h","e","l","l","o"]\n
// @lcpr case=end

// @lcpr case=start
// ["H","a","n","n","a","h"]\n
// @lcpr case=end

 */

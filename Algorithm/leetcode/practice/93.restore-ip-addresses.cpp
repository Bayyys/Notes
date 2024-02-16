/*
 * @lc app=leetcode.cn id=93 lang=cpp
 * @lcpr version=30111
 *
 * [93] 复原 IP 地址
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
  vector<string> res;

  // 回溯算法
  void TV(string& s, int start, int step) {
    if (step == 3) {
      if (isValid(s, start, s.size() - 1)) {
        res.push_back(s);
      }
      return;
    }
    for (int i = start; i < s.size(); i++) {
      if (isValid(s, start, i)) {
        s.insert(s.begin() + i + 1, '.');
        TV(s, i + 2, step + 1);
        s.erase(s.begin() + i + 1);
      } else {
        break;
      }
    }
  }

  // 判断字符串是否合法 (1. 0-255 2. 不能以0开头)
  bool isValid(string& s, int start, int end) {
    if (start > end) {
      return false;
    }
    if (s[start] == '0' && start != end) {
      return false;
    }
    int num = 0;
    for (int i = start; i <= end; i++) {
      if (s[i] > '9' || s[i] < '0') {
        return false;
      }
      num = num * 10 + (s[i] - '0');
      if (num > 255) {
        return false;
      }
    }
    return true;
  }

  vector<string> restoreIpAddresses(string s) {
    TV(s, 0, 0);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "25525511135"\n
// @lcpr case=end

// @lcpr case=start
// "0000"\n
// @lcpr case=end

// @lcpr case=start
// "101023"\n
// @lcpr case=end

 */

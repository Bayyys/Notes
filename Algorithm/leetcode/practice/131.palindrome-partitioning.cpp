/*
 * @lc app=leetcode.cn id=131 lang=cpp
 * @lcpr version=30111
 *
 * [131] 分割回文串
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
  vector<vector<string>> res;
  vector<string> path;
  bool isPalindromic(string& s, int start, int end) {
    while (start < end) {
      if (s[start] != s[end]) return false;
      start++;
      end--;
    }
    return true;
  }
  void TV(int startIndex, string& s) {
    if (startIndex > s.size() - 1) {
      res.push_back(path);
      return;
    }
    for (int i = startIndex; i < s.size(); i++) {
      if (isPalindromic(s, startIndex, i)) {
        path.push_back(s.substr(startIndex, i - startIndex + 1));
        TV(i + 1, s);
        path.pop_back();
      }
    }
  }
  vector<vector<string>> partition(string s) {
    TV(0, s);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "aab"\n
// @lcpr case=end

// @lcpr case=start
// "a"\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=242 lang=cpp
 * @lcpr version=30110
 *
 * [242] 有效的字母异位词
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
  bool isAnagram(string s, string t) {
    int ch_count[26] = {0};
    for (auto ch : s) {
      ch_count[ch - 'a']++;
    }
    for (auto ch : t) {
      if (ch_count[ch - 'a'] == 0) {
        return false;
      }
      ch_count[ch - 'a']--;
    }
    for (auto count : ch_count) {
      if (count != 0) {
        return false;
      }
    }
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "anagram"\n"nagaram"\n
// @lcpr case=end

// @lcpr case=start
// "rat"\n"car"\n
// @lcpr case=end

 */

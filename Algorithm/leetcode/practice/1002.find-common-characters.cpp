/*
 * @lc app=leetcode.cn id=1002 lang=cpp
 * @lcpr version=30114
 *
 * [1002] 查找共用字符
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
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// @lcpr-template-end
// @lc code=start
class Solution {
 public:
  vector<string> commonChars(vector<string> &words) {
    vector<int> cnt_chars(26, INT_MAX);  // 存放每个字符出现的最小次数
    for (auto &word : words) {
      vector<int> cnt_chars_word(26, 0);
      for (auto &c : word) {
        cnt_chars_word[c - 'a']++;
      }
      for (int i = 0; i < 26; i++) {
        cnt_chars[i] = min(cnt_chars[i], cnt_chars_word[i]);
      }
    }
    vector<string> ans;
    for (int i = 0; i < 26; i++) {
      while (cnt_chars[i]--) {
        ans.push_back(string(1, 'a' + i));
      }
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// ["bella","label","roller"]\n
// @lcpr case=end

// @lcpr case=start
// ["cool","lock","cook"]\n
// @lcpr case=end

 */

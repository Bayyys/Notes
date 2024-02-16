/*
 * @lc app=leetcode.cn id=205 lang=cpp
 * @lcpr version=30114
 *
 * [205] 同构字符串
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
  bool isIsomorphic(string s, string t) {
    unordered_map<char, char> m1, m2;
    for (int i = 0; i < s.size(); i++) {
      if (m1.count(s[i]) && m1[s[i]] != t[i]) return false;
      if (m2.count(t[i]) && m2[t[i]] != s[i]) return false;
      m1[s[i]] = t[i];
      m2[t[i]] = s[i];
    }
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "egg"\n"add"\n
// @lcpr case=end

// @lcpr case=start
// "foo"\n"bar"\n
// @lcpr case=end

// @lcpr case=start
// "paper"\n"title"\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=438 lang=cpp
 * @lcpr version=30110
 *
 * [438] 找到字符串中所有字母异位词
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
  vector<int> findAnagrams(string s, string p) {
    if (s.size() < p.size())
      return {};  // 如果s的长度小于p的长度，那么一定不会有答案
    vector<int> ans;
    vector<int> p_cnt(26, 0);
    for (auto& ch : p) ++p_cnt[ch - 'a'];
    for (int l = 0, r = 0; r < s.size(); r++) {
      --p_cnt[s[r] - 'a'];
      while (p_cnt[s[r] - 'a'] < 0) ++p_cnt[s[l++] - 'a'];
      cout << l << " " << r << endl;
      if (r - l + 1 == p.size()) ans.push_back(l);
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "cbaebabacd"\n"abc"\n
// @lcpr case=end

// @lcpr case=start
// "abab"\n"ab"\n
// @lcpr case=end

 */

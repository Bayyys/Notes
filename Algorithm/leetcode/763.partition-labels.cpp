/*
 * @lc app=leetcode.cn id=763 lang=cpp
 * @lcpr version=30112
 *
 * [763] 划分字母区间
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
  vector<int> partitionLabels(string s) {
    int hash[27] = {0};
    for (int i = 0; i < s.size(); i++) {
      hash[s[i] - 'a'] = i;
    }
    vector<int> res;
    int left = 0, right = 0;
    for (int i = 0; i < s.size(); i++) {
      right = max(right, hash[s[i] - 'a']);
      if (i == right) {
        res.push_back(right - left + 1);
        left = right + 1;
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "ababcbacadefegdehijhklij"\n
// @lcpr case=end

// @lcpr case=start
// "eccbbbbdec"\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=350 lang=cpp
 * @lcpr version=30110
 *
 * [350] 两个数组的交集 II
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
  vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> cnt;
    for (auto& num : nums1) {
      cnt[num]++;
    }
    vector<int> ans;
    for (auto& num : nums2) {
      if (cnt[num] > 0) {
        ans.push_back(num);
        cnt[num]--;
      }
    }
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,2,1]\n[2,2]\n
// @lcpr case=end

// @lcpr case=start
// [4,9,5]\n[9,4,9,8,4]\n
// @lcpr case=end

 */

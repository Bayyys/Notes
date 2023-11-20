/*
 * @lc app=leetcode.cn id=454 lang=cpp
 * @lcpr version=30110
 *
 * [454] 四数相加 II
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
  int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3,
                   vector<int>& nums4) {
    unordered_map<int, int> map;  // <sum, count>
    for (auto a : nums1) {
      for (auto b : nums2) {
        map[a + b]++;
      }
    }
    int count = 0;
    for (auto c : nums3) {
      for (auto d : nums4) {
        if (map.find(-c - d) != map.end()) {
          count += map[-c - d];
        }
      }
    }
    return count;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2]\n[-2,-1]\n[-1,2]\n[0,2]\n
// @lcpr case=end

// @lcpr case=start
// [0]\n[0]\n[0]\n[0]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=347 lang=cpp
 * @lcpr version=30110
 *
 * [347] 前 K 个高频元素
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
  struct cmp {
    bool operator()(const pair<int, int>& a, const pair<int, int>& b) {
      return a.second > b.second;
    };
  };

  vector<int> topKFrequent(vector<int>& nums, int k) {
    // 统计元素出现的频率
    unordered_map<int, int> count_map;
    for (auto& num : nums) count_map[num]++;

    // 对频率进行排序(使用小顶堆)
    priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> pq;
    for (auto it = count_map.begin(); it != count_map.end(); it++) {
      pq.push(*it);
      if (pq.size() > k) pq.pop();
    }

    // 输出前k高频元素
    vector<int> res(k);
    for (int i = k - 1; i >= 0; i--) {
      res[i] = pq.top().first;
      pq.pop();
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,1,1,2,2,3]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1]\n1\n
// @lcpr case=end

 */

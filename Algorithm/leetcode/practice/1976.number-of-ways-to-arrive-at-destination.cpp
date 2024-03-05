/*
 * @lc app=leetcode.cn id=1976 lang=cpp
 * @lcpr version=30118
 *
 * [1976] 到达目的地的方案数
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
#include <map>
#include <queue>
#include <set>
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

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

// @lcpr-template-end
// @lc code=start
class Solution {
 private:
  struct cmp {
    bool operator()(pair<int, long long> &a, pair<int, long long> &b) {
      return a.second > b.second;
    };
  };

 public:
  int countPaths(int n, vector<vector<int>> &roads) {
    vector<vector<pair<int, long long>>> g(
        n);  // g[i] = {j, w} 表示从i到j的权重为w
    for (auto &r : roads) {
      g[r[0]].emplace_back(r[1], r[2]);
      g[r[1]].emplace_back(r[0], r[2]);
    }
    vector<long long> dis(n, LLONG_MAX);
    // 更改优先级队列的比较函数
    priority_queue<pair<int, long long>, vector<pair<int, long long>>, cmp> pq;
    vector<long long> ways(n);
    pq.push({0, 0});
    dis[0] = 0;
    ways[0] = 1;
    while (!pq.empty()) {
      auto [next, value] = pq.top();
      pq.pop();
      if (value > dis[next]) continue;
      for (auto [to, w] : g[next]) {
        if (value + w < dis[to]) {
          dis[to] = value + w;
          ways[to] = ways[next];
          pq.push({to, value + w});
        } else if (value + w == dis[to]) {
          ways[to] = (ways[to] + ways[next]) % 1000000007;
        }
      }
    }
    return ways[n - 1];
  }
};
// @lc code=end

/*
// @lcpr case=start
//
7\n[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]\n
// @lcpr case=end

// @lcpr case=start
// 2\n[[1,0,10]]\n
// @lcpr case=end

 */

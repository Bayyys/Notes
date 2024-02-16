/*
 * @lc app=leetcode.cn id=685 lang=cpp
 * @lcpr version=30113
 *
 * [685] 冗余连接 II
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
#define MAXN 1002
class Solution {
 private:
  vector<int> uf = vector<int>(MAXN, 0);
  int cnt = 0;

  void init() {
    for (int i = 0; i < uf.size(); i++) {
      uf[i] = i;
    }
  }

  int find(int u) { return u == uf[u] ? u : uf[u] = find(uf[u]); }

  bool isSame(int u, int v) { return find(u) == find(v); }

  void join(int u, int v) {
    u = find(u);
    v = find(v);
    if (u == v) return;
    uf[u] = v;
  }

 public:
  vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
    vector<int> inDegree = vector<int>(MAXN, 0);  // 记录节点的入度
    cnt = edges.size();
    for (auto& edge : edges) {
      inDegree[edge[1]]++;
    }
    vector<int> vec_in2;  // 记录入度为2的节点
    for (int i = cnt - 1; i >= 0; i--) {
      if (inDegree[edges[i][1]] == 2) {
        vec_in2.push_back(i);
      }
    }
    // 如果存在入度为2的节点，那么一定是有向环的一部分
    if (vec_in2.size() > 0) {
      init();
      for (int i = 0; i < cnt; i++) {
        if (i == vec_in2[0]) continue;
        if (isSame(edges[i][0], edges[i][1])) {
          return edges[vec_in2[1]];
        }
        join(edges[i][0], edges[i][1]);
      }
      return edges[vec_in2[0]];
    } else {  // 如果不存在入度为2的节点，那么一定是有向环
      init();
      for (auto& edge : edges) {
        if (isSame(edge[0], edge[1])) {
          return edge;
        }
        join(edge[0], edge[1]);
      }
    }
    return {0, 0};
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[1,2],[1,3],[2,3]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2],[2,3],[3,4],[4,1],[1,5]]\n
// @lcpr case=end

 */

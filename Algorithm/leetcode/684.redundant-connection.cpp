/*
 * @lc app=leetcode.cn id=684 lang=cpp
 * @lcpr version=30113
 *
 * [684] 冗余连接
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
  vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    init();
    for (auto edge : edges) {
      if (isSame(edge[0], edge[1]))
        return edge;
      else
        join(edge[0], edge[1]);
    }
    return vector<int>{};
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[1,2], [1,3], [2,3]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2], [2,3], [3,4], [1,4], [1,5]]\n
// @lcpr case=end

 */

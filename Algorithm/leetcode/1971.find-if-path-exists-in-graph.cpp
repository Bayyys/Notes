/*
 * @lc app=leetcode.cn id=1971 lang=cpp
 * @lcpr version=30113
 *
 * [1971] 寻找图中是否存在路径
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
#define MAXN 2 * 10e5 + 1
class Solution {
 private:
  vector<int> union_find = vector<int>(MAXN, 0);

  void init() {
    for (int i = 0; i < MAXN; i++) {
      union_find[i] = i;
    }
  }

  int find(int u) {
    return u == union_find[u] ? u : union_find[u] = find(union_find[u]);
  }

  bool isSame(int u, int v) {
    u = find(u);
    v = find(v);
    return u == v;
  }

  void join(int u, int v) {
    u = find(u);
    v = find(v);
    if (u == v) return;
    union_find[u] = v;
  }

 public:
  bool validPath(int n, vector<vector<int>>& edges, int source,
                 int destination) {
    init();
    for (auto edge : edges) {
      join(edge[0], edge[1]);
    }
    return isSame(source, destination);
  }
};
// @lc code=end

/*
// @lcpr case=start
// 3\n[[0,1],[1,2],[2,0]]\n0\n2\n
// @lcpr case=end

// @lcpr case=start
// 6\n[[0,1],[0,2],[3,5],[5,4],[4,3]]\n0\n5\n
// @lcpr case=end

 */

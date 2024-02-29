/*
 * @lc app=leetcode.cn id=2581 lang=cpp
 * @lcpr version=30117
 *
 * [2581] 统计可能的树根数目
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
  int g_cnt = 0;
  int ans = 0;
  int goal = 0;
  void dfs(vector<vector<int>> &g, set<pair<int, int>> &guesses, int node,
           int parent) {
    for (auto &e : g[node]) {
      if (e == parent) continue;
      if (guesses.find({node, e}) != guesses.end()) {
        g_cnt++;
      }
      dfs(g, guesses, e, node);
    }
  }

  void dfs2(vector<vector<int>> &g, set<pair<int, int>> &guesses, int node,
            int parent, int cur_cnt) {
    for (auto &e : g[node]) {
      if (e == parent) continue;
      int c = cur_cnt;
      if (guesses.find({node, e}) != guesses.end()) {
        c--;
      }
      if (guesses.find({e, node}) != guesses.end()) {
        c++;
      }
      dfs2(g, guesses, e, node, c);
      if (c >= goal) ans++;
    }
  }

 public:
  int rootCount(vector<vector<int>> &edges, vector<vector<int>> &guesses,
                int k) {
    int n = edges.size() + 1;  // 节点数
    goal = k;
    vector<vector<int>> g(n + 1);  // 邻接表
    for (auto &e : edges) {
      g[e[0]].push_back(e[1]);
      g[e[1]].push_back(e[0]);
    }
    set<pair<int, int>> gue;  // 猜想集合
    for (auto &e : guesses) {
      gue.insert({e[0], e[1]});
    }
    // 假设 0 为根节点, 计算正确猜想数目
    dfs(g, gue, 0, -1);

    // 分别改变根节点, 计算正确猜想数目
    ans = g_cnt >= k ? 1 : 0;
    dfs2(g, gue, 0, -1, g_cnt);

    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[0,1],[1,2],[1,3],[4,2]]\n[[1,3],[0,1],[1,0],[2,4]]\n3\n
// @lcpr case=end

// @lcpr case=start
// [[0,1],[1,2],[2,3],[3,4]]\n[[1,0],[3,4],[2,1],[3,2]]\n1\n
// @lcpr case=end

 */

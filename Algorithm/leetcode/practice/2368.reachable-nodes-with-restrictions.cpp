/*
 * @lc app=leetcode.cn id=2368 lang=cpp
 * @lcpr version=30117
 *
 * [2368] 受限条件下可到达节点的数目
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
 public:
  int reachableNodes(int n, vector<vector<int>> &edges,
                     vector<int> &restricted) {
    vector<vector<int>> g(n);
    set<int> ignore_nodes;
    int ans = 0;
    for (auto &r : restricted) ignore_nodes.insert(r);
    for (auto &e : edges) {
      if (ignore_nodes.find(e[0]) == ignore_nodes.end() &&
          ignore_nodes.find(e[1]) == ignore_nodes.end()) {
        g[e[0]].emplace_back(e[1]);
        g[e[1]].emplace_back(e[0]);
      }
    }
    auto dfs = [&](auto self, int node, int fa) -> void {
      for (auto &n : g[node]) {
        // cout << "node: " << node << " n: " << n << endl;
        if (n == fa) continue;
        ans++;
        self(self, n, node);
      }
    };
    ans++;
    dfs(dfs, 0, -1);
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// 7\n[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]\n[4,5]\n
// @lcpr case=end

// @lcpr case=start
// 7\n[[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]\n[4,2,1]\n
// @lcpr case=end

 */

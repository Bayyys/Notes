/*
 * @lc app=leetcode.cn id=797 lang=cpp
 * @lcpr version=30113
 *
 * [797] 所有可能的路径
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
 private:
  vector<vector<int>> ans;
  vector<int> path;
  void dfs(vector<vector<int>>& graph, int x) {
    if (x == graph.size() - 1) {  // 到达终点(n-1)
      ans.push_back(path);
      return;
    }
    for (int i = 0; i < graph[x].size(); i++) {
      path.push_back(graph[x][i]);
      dfs(graph, graph[x][i]);
      path.pop_back();
    }
  }

 public:
  vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
    path.push_back(0);
    dfs(graph, 0);
    return ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[1,2],[3],[3],[]]\n
// @lcpr case=end

// @lcpr case=start
// [[4,3,1],[3,2,4],[3],[4],[]]\n
// @lcpr case=end

 */

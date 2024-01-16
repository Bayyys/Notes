/*
 * @lc app=leetcode.cn id=417 lang=cpp
 * @lcpr version=30113
 *
 * [417] 太平洋大西洋水流问题
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
  vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

  void dfs(vector<vector<int>>& heights, vector<vector<vector<bool>>>& visited,
           int x, int y, int pos) {
    visited[x][y][pos] = true;
    for (auto& dir : dirs) {
      int nx = x + dir[0], ny = y + dir[1];
      if (nx < 0 || nx >= heights.size() || ny < 0 || ny >= heights[0].size() ||
          visited[nx][ny][pos] || heights[nx][ny] < heights[x][y]) {
        continue;
      }
      dfs(heights, visited, nx, ny, pos);
    }
  }

 public:
  vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
    // 从边缘开始深度搜索, 进行标记 {1, 1} 表示左/上边界, 右/下边界能抵达
    vector<vector<vector<bool>>> visited = vector<vector<vector<bool>>>(
        heights.size(),
        vector<vector<bool>>(heights[0].size(), vector<bool>(2, false)));
    for (int i = 0; i < heights.size(); i++) {
      if (!visited[i][0][0]) {
        dfs(heights, visited, i, 0, 0);
      }
      if (!visited[i][heights[0].size() - 1][1]) {
        dfs(heights, visited, i, heights[0].size() - 1, 1);
      }
    }
    for (int i = 0; i < heights[0].size(); i++) {
      if (!visited[0][i][0]) {
        dfs(heights, visited, 0, i, 0);
      }
      if (!visited[heights.size() - 1][i][1]) {
        dfs(heights, visited, heights.size() - 1, i, 1);
      }
    }
    vector<vector<int>> res;
    for (int i = 0; i < heights.size(); i++) {
      for (int j = 0; j < heights[0].size(); j++) {
        if (visited[i][j][0] && visited[i][j][1]) {
          res.push_back({i, j});
        }
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]\n
// @lcpr case=end

// @lcpr case=start
// [[2,1],[1,2]]\n
// @lcpr case=end

 */

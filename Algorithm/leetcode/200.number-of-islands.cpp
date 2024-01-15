/*
 * @lc app=leetcode.cn id=200 lang=cpp
 * @lcpr version=30113
 *
 * [200] 岛屿数量
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
  int direction[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  void dfs(vector<vector<char>>& grid, vector<vector<bool>>& visited, int x,
           int y) {
    if (visited[x][y] || grid[x][y] == '0') return;
    visited[x][y] = true;
    for (int i = 0; i < 4; i++) {  // 向四周扩散
      int nx = x + direction[i][0];
      int ny = y + direction[i][1];
      if (nx >= 0 && nx < grid.size() && ny >= 0 &&
          ny < grid[0].size())  // 只要不越界就继续dfs
        dfs(grid, visited, nx, ny);
    }
  }
  void bfs(vector<vector<char>>& grid, vector<vector<bool>>& visited, int x,
           int y) {
    queue<pair<int, int>> que;
    que.push({x, y});
    visited[x][y] = true;
    while (!que.empty()) {
      pair<int, int> cur = que.front();
      que.pop();
      int cx = cur.first, cy = cur.second;
      for (int i = 0; i < 4; i++) {
        int nx = cx + direction[i][0];
        int ny = cy + direction[i][1];
        if (nx >= 0 && nx < grid.size() && ny >= 0 &&
            ny < grid[0].size())  // 只要不越界就继续dfs
          if (!visited[nx][ny] && grid[nx][ny] == '1') {
            que.push({nx, ny});
            visited[nx][ny] = true;
          }
      }
    }
  }

 public:
  int numIslands(vector<vector<char>>& grid) {
    int row = grid.size(), col = grid[0].size();
    vector<vector<bool>> visited(row, vector<bool>(col, false));
    int res = 0;
    for (int i = 0; i < row; i++)
      for (int j = 0; j < col; j++) {
        if (!visited[i][j] && grid[i][j] == '1') {
          res++;
          bfs(grid, visited, i, j);
        }
      }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
//
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
// @lcpr case=end

// @lcpr case=start
//
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
// @lcpr case=end

 */

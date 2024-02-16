/*
 * @lc app=leetcode.cn id=1020 lang=cpp
 * @lcpr version=30113
 *
 * [1020] 飞地的数量
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
  int count;
  int direction[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  void dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x,
           int y) {
    count++;
    visited[x][y] = true;
    for (int i = 0; i < 4; i++) {
      int nx = x + direction[i][0];
      int ny = y + direction[i][1];
      if (nx >= 0 && nx < grid.size() && ny >= 0 && ny < grid[0].size() &&
          !visited[nx][ny] && grid[nx][ny] == 1)
        dfs(grid, visited, nx, ny);
    }
  }

  void bfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x,
           int y) {
    count++;
    queue<pair<int, int>> que;
    que.push({x, y});
    grid[x][y] = 0;
    visited[x][y] = true;
    while (!que.empty()) {
      auto [x, y] = que.front();
      que.pop();
      for (int i = 0; i < 4; i++) {
        int nx = x + direction[i][0];
        int ny = y + direction[i][1];
        if (nx >= 0 && nx < grid.size() && ny >= 0 && ny < grid[0].size() &&
            !visited[nx][ny] && grid[nx][ny] == 1) {
          que.push({nx, ny});
          count++;
          visited[nx][ny] = true;
        }
      }
    }
  }

 public:
  int numEnclaves(vector<vector<int>>& grid) {
    int row = grid.size(), col = grid[0].size();
    vector<vector<bool>> visited(row, vector<bool>(col, false));
    for (int i = 0; i < row; i++) {
      if (grid[i][0] == 1) dfs(grid, visited, i, 0);
      if (grid[i][col - 1] == 1) dfs(grid, visited, i, col - 1);
    }
    for (int i = 0; i < col; i++) {
      if (grid[0][i] == 1) dfs(grid, visited, 0, i);
      if (grid[row - 1][i] == 1) dfs(grid, visited, row - 1, i);
    }
    count = 0;
    for (int i = 0; i < row; i++)
      for (int j = 0; j < col; j++)
        if (!visited[i][j] && grid[i][j] == 1) {
          bfs(grid, visited, i, j);
        }
    return count;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]\n
// @lcpr case=end

 */

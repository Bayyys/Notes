/*
 * @lc app=leetcode.cn id=827 lang=cpp
 * @lcpr version=30113
 *
 * [827] 最大人工岛
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
  int mark = 2;
  int count = 0;
  void dfs(vector<vector<int>>& grid, int x, int y) {
    grid[x][y] = mark;
    for (auto xy : direction) {
      int nx = x + xy[0], ny = y + xy[1];
      if (nx >= 0 && nx < grid.size() && ny >= 0 && ny < grid[0].size() &&
          grid[nx][ny] == 1) {
        count++;
        dfs(grid, nx, ny);
      }
    }
  }

 public:
  int largestIsland(vector<vector<int>>& grid) {
    // 给每个岛屿进行编号, 若为0则为未编号
    // 记录每个岛屿的面积
    // 依次遍历0, 向四周扩展, 记录最大值
    int row = grid.size(), col = grid[0].size();
    unordered_map<int, int> area_map;  // 岛屿编号 -> 面积
    // 1. 给每个岛屿编号, 并记录面积
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        if (grid[i][j] == 1) {
          count = 1;
          dfs(grid, i, j);
          area_map[mark] = count;
          mark++;
        }
      }
    }
    int res = 0;
    // 2. 记录岛屿最大值
    for (auto& [k, v] : area_map) {
      res = max(res, v);
    }
    // 3. 遍历0, 向四周扩展, 记录岛屿面积相加最大值
    unordered_set<int> visited;
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        if (grid[i][j] == 0) {
          visited.clear();
          count = 1;
          for (auto& xy : direction) {
            int nx = i + xy[0], ny = j + xy[1];
            if (nx >= 0 && nx < row && ny >= 0 && ny < col &&
                grid[nx][ny] > 1 &&
                visited.find(grid[nx][ny]) == visited.end()) {
              count += area_map[grid[nx][ny]];
              visited.insert(grid[nx][ny]);
            }
          }
          res = max(res, count);
        }
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[1, 0], [0, 1]]\n
// @lcpr case=end

// @lcpr case=start
// [[1, 1], [1, 0]]\n
// @lcpr case=end

// @lcpr case=start
// [[1, 1], [1, 1]]\n
// @lcpr case=end

 */

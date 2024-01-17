/*
 * @lc app=leetcode.cn id=463 lang=cpp
 * @lcpr version=30113
 *
 * [463] 岛屿的周长
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
  int direaction[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

 public:
  int islandPerimeter(vector<vector<int>>& grid) {
    int res = 0;
    for (int i = 0; i < grid.size(); i++) {
      for (int j = 0; j < grid[0].size(); j++) {
        if (grid[i][j] == 1) {
          for (int k = 0; k < 4; k++) {
            int x = i + direaction[k][0];
            int y = j + direaction[k][1];
            if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size() ||
                grid[x][y] == 0) {
              res++;
            }
          }
        }
      }
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[1]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,0]]\n
// @lcpr case=end

 */

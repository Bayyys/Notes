/*
 * @lc app=leetcode.cn id=51 lang=cpp
 * @lcpr version=30111
 *
 * [51] N 皇后
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
 public:
  vector<vector<string>> res;
  vector<string> path;
  void TV(const int n, int row) {
    if (row == n) {
      res.push_back(path);
      return;
    }
    for (int col = 0; col < n; col++) {
      if (check(row, col, n)) {
        path[row][col] = 'Q';
        TV(n, row + 1);
        path[row][col] = '.';
      }
    }
  }

  bool check(int row, int col, int n) {
    for (int i = 0; i < row; i++) {
      if (path[i][col] == 'Q') return false;
    }
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
      if (path[i][j] == 'Q') return false;
    }
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
      if (path[i][j] == 'Q') return false;
    }
    return true;
  }

  vector<vector<string>> solveNQueens(int n) {
    path.resize(n, string(n, '.'));
    TV(n, 0);
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// 4\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */

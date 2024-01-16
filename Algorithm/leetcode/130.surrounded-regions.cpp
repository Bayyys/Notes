/*
 * @lc app=leetcode.cn id=130 lang=cpp
 * @lcpr version=30113
 *
 * [130] 被围绕的区域
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
  vector<vector<char>> ans;
  int direction[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  void bfs(vector<vector<char>>& board, vector<vector<bool>>& visited, int x,
           int y) {
    queue<pair<int, int>> que;
    que.push({x, y});
    ans[x][y] = 'O';
    visited[x][y] = true;
    while (!que.empty()) {
      auto [x, y] = que.front();
      que.pop();
      for (int i = 0; i < 4; i++) {
        int nx = x + direction[i][0];
        int ny = y + direction[i][1];
        if (nx >= 0 && nx < board.size() && ny >= 0 && ny < board[0].size() &&
            board[nx][ny] == 'O' && !visited[nx][ny]) {
          que.push({nx, ny});
          visited[nx][ny] = true;
          ans[nx][ny] = 'O';
        }
      }
    }
  }

 public:
  void solve(vector<vector<char>>& board) {
    ans =
        vector<vector<char>>(board.size(), vector<char>(board[0].size(), 'X'));
    vector<vector<bool>> visited = vector<vector<bool>>(
        board.size(), vector<bool>(board[0].size(), false));
    for (int i = 0; i < board.size(); i++) {
      if (board[i][0] == 'O' && !visited[i][0]) bfs(board, visited, i, 0);
      if (board[i][board[0].size() - 1] == 'O' &&
          !visited[i][board[0].size() - 1])
        bfs(board, visited, i, board[0].size() - 1);
    }
    for (int i = 0; i < board[0].size(); i++) {
      if (board[0][i] == 'O' && !visited[0][i]) bfs(board, visited, 0, i);
      if (board[board.size() - 1][i] == 'O' && !visited[board.size() - 1][i])
        bfs(board, visited, board.size() - 1, i);
    }
    board = ans;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
// @lcpr case=end

// @lcpr case=start
// [["X"]]\n
// @lcpr case=end

 */

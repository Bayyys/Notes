/*
 * @lc app=leetcode.cn id=37 lang=cpp
 * @lcpr version=30111
 *
 * [37] 解数独
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
  bool TV(vector<vector<char>>& board) {
    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; ++j) {
        if (board[i][j] == '.') {
          for (char c = '1'; c <= '9'; c++) {
            if (check(i, j, c, board)) {
              board[i][j] = c;
              if (TV(board)) {
                return true;
              }
              board[i][j] = '.';
            }
          }
          return false;
        }
      }
    }
    return true;
  }

  bool check(int row, int col, char val, vector<vector<char>>& board) {
    for (int i = 0; i < 9; i++) {
      if (board[row][i] == val) {
        return false;
      }
      if (board[i][col] == val) {
        return false;
      }
      if (board[(row / 3) * 3 + i / 3][(col / 3) * 3 + i % 3] == val) {
        return false;
      }
    }
    return true;
  }

  void solveSudoku(vector<vector<char>>& board) { TV(board); }
};
// @lc code=end

/*
// @lcpr case=start
//
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
// @lcpr case=end

 */

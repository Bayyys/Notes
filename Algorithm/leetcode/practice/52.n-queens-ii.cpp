/*
 * @lc app=leetcode.cn id=52 lang=cpp
 * @lcpr version=30114
 *
 * [52] N 皇后 II
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
 private:
  int cnt = 0;

  void TV(int n, int row, vector<vector<int>> &chess) {
    if (row == n) {
      cnt++;
      return;
    }
    for (int col = 0; col < n; col++) {
      if (check(row, col, chess, n)) {
        chess[row][col] = 1;
        TV(n, row + 1, chess);
        chess[row][col] = 0;
      }
    }
  }

  bool check(int row, int col, vector<vector<int>> &chess, int n) {
    for (int i = 0; i < row; i++) {
      if (chess[i][col] == 1) return false;
    }
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
      if (chess[i][j] == 1) return false;
    }
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
      if (chess[i][j] == 1) return false;
    }
    return true;
  }

 public:
  int totalNQueens(int n) {
    vector<vector<int>> chess(n, vector<int>(n, 0));
    TV(n, 0, chess);
    return cnt;
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

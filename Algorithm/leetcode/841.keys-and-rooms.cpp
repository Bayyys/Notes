/*
 * @lc app=leetcode.cn id=841 lang=cpp
 * @lcpr version=30113
 *
 * [841] 钥匙和房间
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
  void dfs(vector<vector<int>>& rooms, vector<bool>& visited, int pos) {
    vector<int> keys = rooms[pos];
    for (int key : keys) {
      if (!visited[key]) {
        visited[key] = true;
        dfs(rooms, visited, key);
      }
    }
  }

 public:
  bool canVisitAllRooms(vector<vector<int>>& rooms) {
    vector<bool> visited =  // visited[i] 表示房间 i 是否被访问过
        vector<bool>(rooms.size(), false);
    visited[0] = true;
    dfs(rooms, visited, 0);
    for (bool v : visited) {
      if (!v) return false;
    }
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[1],[2],[3],[]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,3],[3,0,1],[2],[0]]\n
// @lcpr case=end

 */

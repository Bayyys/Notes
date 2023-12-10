/*
 * @lc app=leetcode.cn id=332 lang=cpp
 * @lcpr version=30111
 *
 * [332] 重新安排行程
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
  vector<string> res;
  unordered_map<string, map<string, int>>
      graph;  // undered_map<出发机场, map<到达机场, 航班次数>> graph;
  int spent = 0;
  bool TV() {
    if (res.size() == spent + 1) {
      // 所有机票都用完了
      return true;
    }
    for (auto& [to, count] : graph[res[res.size() - 1]]) {
      if (count > 0) {
        res.push_back(to);
        count--;
        if (TV()) {
          return true;
        }
        res.pop_back();
        count++;
      }
    }
    return false;
  }

  vector<string> findItinerary(vector<vector<string>>& tickets) {
    for (auto& ticket : tickets) {
      graph[ticket[0]][ticket[1]]++;
    }
    res.push_back("JFK");
    spent = tickets.size();
    TV();
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]\n
// @lcpr case=end

// @lcpr case=start
// [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]\n
// @lcpr case=end

 */

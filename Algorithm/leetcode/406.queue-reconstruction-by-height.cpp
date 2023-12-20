/*
 * @lc app=leetcode.cn id=406 lang=cpp
 * @lcpr version=30112
 *
 * [406] 根据身高重建队列
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
  vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
    sort(people.begin(), people.end(),
         [](const vector<int>& a, const vector<int>& b) {
           return a[0] == b[0] ? a[1] < b[1] : a[0] > b[0];
         });
    // 直接以函数作为参数，不用写成类的成员函数
    list<vector<int>> que;
    for (auto& p : people) {
      auto it = que.begin();
      advance(it, p[1]);  // 从前往后插入，插入位置为p[1]
      // 注: advance(it, n) 增加给定的迭代器 it 向前 n 个元素的位置
      que.insert(it, p);
    }
    return vector<vector<int>>(que.begin(), que.end());
  }
};
// @lc code=end

/*
// @lcpr case=start
// [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]\n
// @lcpr case=end

// @lcpr case=start
// [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]\n
// @lcpr case=end

 */

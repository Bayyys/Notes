/*
 * @lc app=leetcode.cn id=84 lang=cpp
 * @lcpr version=30112
 *
 * [84] 柱状图中最大的矩形
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
  int largestRectangleArea(vector<int>& heights) {
    stack<int> st;
    heights.push_back(0);
    heights.insert(heights.begin(), 0);
    st.push(0);
    int res = 0;
    for (int i = 1; i < heights.size(); i++) {
      while (heights[i] < heights[st.top()]) {
        int mid = st.top();
        st.pop();
        int w = i - st.top() - 1;
        int h = heights[mid];
        res = max(res, w * h);
      }
      st.push(i);
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [2,1,5,6,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [2,4]\n
// @lcpr case=end

 */

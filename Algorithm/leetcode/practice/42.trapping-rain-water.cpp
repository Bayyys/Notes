/*
 * @lc app=leetcode.cn id=42 lang=cpp
 * @lcpr version=30112
 *
 * [42] 接雨水
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
  int trap(vector<int>& height) {
    stack<int> st;
    int res = 0;
    st.push(0);
    for (int i = 1; i < height.size(); i++) {
      while (!st.empty() && height[i] > height[st.top()]) {
        int top = st.top();
        st.pop();
        if (!st.empty()) {
          int left = st.top();
          int right = i;
          int h = min(height[left], height[right]) - height[top];
          res += h * (right - left - 1);
        }
      }
      st.push(i);
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [0,1,0,2,1,0,1,3,2,1,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [4,2,0,3,2,5]\n
// @lcpr case=end

 */

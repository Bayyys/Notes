/*
 * @lc app=leetcode.cn id=239 lang=cpp
 * @lcpr version=30110
 *
 * [239] 滑动窗口最大值
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
  class MyQueue {
   private:
    deque<int> q;  // 使用deque实现单调队列(单调递减)

   public:
    // 队列front()是最大值, 滑动窗口移动时, 如果front()是移除的元素,
    // 则pop_front()
    void pop(int value) {
      if (!q.empty() && value == q.front()) q.pop_front();
    }

    // 如果push的元素比队列back()的元素大, 则将队列中的元素出队,
    // 直到队列为空或者 push的元素小于队列中的元素
    // 以此保证队列中的元素是单调递减的
    void push(int value) {
      while (!q.empty() && value > q.back()) q.pop_back();
      q.push_back(value);
    }

    // 返回队列中的最大值(即队列front())
    int front() { return q.front(); }
  };

 public:
  vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    MyQueue q;
    vector<int> res;
    for (int i = 0; i < k; i++) q.push(nums[i]);
    res.push_back(q.front());
    for (int i = k; i < nums.size(); i++) {
      q.pop(nums[i - k]);  // 移除滑动窗口最左边的元素
      q.push(nums[i]);     // 添加滑动窗口最右边的元素
      res.push_back(q.front());
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,3,-1,-3,5,3,6,7]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1]\n1\n
// @lcpr case=end

 */

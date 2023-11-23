/*
 * @lc app=leetcode.cn id=232 lang=cpp
 * @lcpr version=30110
 *
 * [232] 用栈实现队列
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
class MyQueue {
 public:
  stack<int> sIn;
  stack<int> sOut;
  MyQueue() {}

  void push(int x) { sIn.push(x); }

  int pop() {
    if (sOut.empty()) {
      while (!sIn.empty()) {
        sOut.push(sIn.top());
        sIn.pop();
      }
    }
    int result = sOut.top();
    sOut.pop();
    return result;
  }

  int peek() {
    // if (sOut.empty()) {
    //   while (!sIn.empty()) {
    //     sOut.push(sIn.top());
    //     sIn.pop();
    //   }
    // }
    // return sOut.top();
    int res = this->pop();
    sOut.push(res);
    return res;
  }

  bool empty() { return sIn.empty() && sOut.empty(); }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
// @lc code=end

/*
// @lcpr case=start
// ["MyQueue", "push", "push", "peek", "pop", "empty"][[], [1], [2], [], [],
[]]\n
// @lcpr case=end

 */

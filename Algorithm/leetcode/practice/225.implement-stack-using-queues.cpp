/*
 * @lc app=leetcode.cn id=225 lang=cpp
 * @lcpr version=30110
 *
 * [225] 用队列实现栈
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
class MyStack {
 public:
  queue<int> q;
  MyStack() {}

  void push(int x) { q.push(x); }

  int pop() {
    int size = q.size();
    size--;
    while (size--) {
      q.push(q.front());
      q.pop();
    }
    int res = q.front();
    q.pop();
    return res;
  }

  int top() { return q.back(); }

  bool empty() { return q.empty(); }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
// @lc code=end

/*
// @lcpr case=start
// ["MyStack", "push", "push", "top", "pop", "empty"][[], [1], [2], [], [],
[]]\n
// @lcpr case=end

 */

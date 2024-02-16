/*
 * @lc app=leetcode.cn id=150 lang=cpp
 * @lcpr version=30110
 *
 * [150] 逆波兰表达式求值
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
  int evalRPN(vector<string>& tokens) {
    stack<long long> st;
    for (auto& t : tokens) {
      if (t == "+" || t == "-" || t == "*" || t == "/") {
        long long num2 = st.top();
        st.pop();  // 注意顺序: 先出栈的是右操作数
        long long num1 = st.top();
        st.pop();
        if (t == "+") {
          st.push(num1 + num2);
        } else if (t == "-") {
          st.push(num1 - num2);
        } else if (t == "*") {
          st.push(num1 * num2);
        } else if (t == "/") {
          st.push(num1 / num2);
        }
      } else {
        st.push(stoll(t));
      }
    }
    int res = st.top();
    st.pop();
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// ["2","1","+","3","*"]\n
// @lcpr case=end

// @lcpr case=start
// ["4","13","5","/","+"]\n
// @lcpr case=end

// @lcpr case=start
// ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
// @lcpr case=end

 */

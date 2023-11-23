/*
 * @lc app=leetcode.cn id=20 lang=cpp
 * @lcpr version=30110
 *
 * [20] 有效的括号
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
  bool isValid(string s) {
    // 长度必须为偶数
    if (s.size() % 2 == 1) return false;
    stack<char> st;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '(')
        st.push(')');
      else if (s[i] == '[')
        st.push(']');
      else if (s[i] == '{')
        st.push('}');
      else if (st.empty() ||
               st.top() !=
                   s[i])  // 1. 遇到右括号但是栈已空; 2. 右括号与栈顶不匹配
        return false;
      else
        st.pop();
    }
    return st.empty();
  }
};
// @lc code=end

/*
// @lcpr case=start
// "()"\n
// @lcpr case=end

// @lcpr case=start
// "()[]{}"\n
// @lcpr case=end

// @lcpr case=start
// "(]"\n
// @lcpr case=end

 */

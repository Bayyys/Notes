/*
 * @lc app=leetcode.cn id=925 lang=cpp
 * @lcpr version=30114
 *
 * [925] 长按键入
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
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// @lcpr-template-end
// @lc code=start
class Solution {
 public:
  bool isLongPressedName(string name, string typed) {
    int i = 0, j = 0;
    while (i < name.size() && j < typed.size()) {
      if (name[i] == typed[j]) {
        i++;
        j++;
      } else if (j > 0 && typed[j] == typed[j - 1]) {
        j++;
      } else {
        return false;
      }
    }
    while (j < typed.size() && typed[j] == typed[j - 1]) j++;
    return i == name.size() && j == typed.size();
  }
};
// @lc code=end

/*
// @lcpr case=start
// "alex"\n"aaleex"\n
// @lcpr case=end

// @lcpr case=start
// "saeed"\n"ssaaedd"\n
// @lcpr case=end

 */

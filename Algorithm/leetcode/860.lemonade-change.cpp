/*
 * @lc app=leetcode.cn id=860 lang=cpp
 * @lcpr version=30112
 *
 * [860] 柠檬水找零
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
  bool lemonadeChange(vector<int>& bills) {
    int five = 0, ten = 0;
    for (auto& bill : bills) {
      if (bill == 5) {
        five++;
      } else if (bill == 10) {
        if (five == 0) return false;
        five--;
        ten++;
      } else {
        if (five > 0 && ten > 0) {
          five--;
          ten--;
        } else if (five >= 3) {
          five -= 3;
        } else {
          return false;
        }
      }
    }
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [5,5,5,10,20]\n
// @lcpr case=end

// @lcpr case=start
// [5,5,10,10,20]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=202 lang=cpp
 * @lcpr version=30110
 *
 * [202] 快乐数
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
  bool isHappy(int n) {
    unordered_set<int> set;
    while (1) {
      int sum = compute_happy_sum(n);
      cout << sum << endl;
      if (sum == 1) {  // happy
        return true;
      }
      if (set.find(sum) != set.end()) {  // unhappy
        return false;
      } else {
        set.insert(sum);
      }
      n = sum;
    }
  }

  int compute_happy_sum(int n) {
    int sum = 0;
    while (n) {
      int digit = n % 10;
      sum += digit * digit;
      n /= 10;
    }
    return sum;
  }
};
// @lc code=end

/*
// @lcpr case=start
// 19\n
// @lcpr case=end

// @lcpr case=start
// 2\n
// @lcpr case=end

 */

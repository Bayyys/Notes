/*
 * @lc app=leetcode.cn id=941 lang=cpp
 * @lcpr version=30113
 *
 * [941] 有效的山脉数组
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
  bool validMountainArray(vector<int>& arr) {
    int length = arr.size();
    int left = 0, right = length - 1;
    while (left < right && arr[left] < arr[left + 1]) left++;
    while (right > left && arr[right] < arr[right - 1]) right--;
    if (left == 0 || right == length - 1 || left != right) return false;
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [2,1]\n
// @lcpr case=end

// @lcpr case=start
// [3,5,5]\n
// @lcpr case=end

// @lcpr case=start
// [0,3,2,1]\n
// @lcpr case=end

 */

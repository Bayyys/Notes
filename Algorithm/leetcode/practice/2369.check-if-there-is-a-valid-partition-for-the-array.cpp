/*
 * @lc app=leetcode.cn id=2369 lang=cpp
 * @lcpr version=30117
 *
 * [2369] 检查数组是否存在有效划分
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
#include <map>
#include <queue>
#include <set>
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

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

// @lcpr-template-end
// @lc code=start
class Solution {
 private:
  bool check(vector<int> &nums, int l, int r) {
    l = l - 1, r = r - 1;
    int n = r - l + 1;
    if (n == 1)
      return false;
    else if (n == 2)
      return nums[l] == nums[r];
    else {
      if (nums[r] == nums[r - 1] && nums[r - 1] == nums[r - 2])
        return true;
      else {
        return (nums[l] + 1 == nums[l + 1] && nums[l + 1] + 1 == nums[r])
                   ? true
                   : false;
      }
    }
  }

 public:
  bool validPartition(vector<int> &nums) {
    // dp[i] 表示前 i 个数是否存在有效划分
    // dp[i] = dp[i-2] && check(nums[i-2, i]) || dp[i-3] && check(nums[i-3, i])
    int n = nums.size();
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    dp[2] = check(nums, 1, 2);
    for (int i = 3; i <= n; i++) {
      dp[i] = (dp[i - 2] && check(nums, i - 1, i)) ||
              (dp[i - 3] && check(nums, i - 2, i));
    }
    for (int i = 1; i <= n; i++) cout << dp[i] << " ";
    cout << endl;
    return dp[n];
  }
};
// @lc code=end

/*
// @lcpr case=start
// [4,4,4,5,6]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,2]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=649 lang=cpp
 * @lcpr version=30114
 *
 * [649] Dota2 参议院
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
 public:
  string predictPartyVictory(string senate) {
    bool R = true, D = true;
    int R_cnt = 0, D_cnt = 0;
    while (R && D) {
      R = D = false;
      for (int i = 0; i < senate.size(); i++) {
        if (senate[i] == 'R') {
          if (D_cnt > 0) {
            D_cnt--;
            senate[i] = 'X';
          } else {
            R_cnt++;
            R = true;
          }
        } else if (senate[i] == 'D') {
          if (R_cnt > 0) {
            R_cnt--;
            senate[i] = 'X';
          } else {
            D_cnt++;
            D = true;
          }
        }
      }
    }
    return R ? "Radiant" : "Dire";
  }
};
// @lc code=end

/*
// @lcpr case=start
// "RD"\n
// @lcpr case=end

// @lcpr case=start
// "RDD"\n
// @lcpr case=end

 */

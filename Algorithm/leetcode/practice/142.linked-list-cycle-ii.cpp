/*
 * @lc app=leetcode.cn id=142 lang=cpp
 * @lcpr version=30109
 *
 * [142] 环形链表 II
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
  ListNode(int x) : val(x), next(NULL) {}
};
// @lcpr-template-end
// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
 public:
  ListNode *detectCycle(ListNode *head) {
    ListNode *fast = head;
    ListNode *slow = head;
    while (fast && fast->next) {
      slow = slow->next;        // 慢指针每次走一步
      fast = fast->next->next;  // 快指针每次走两步
      // 快慢指针相遇
      if (slow == fast) {
        ListNode *index1 = fast;
        ListNode *index2 = head;
        while (index1 != index2) {
          index1 = index1->next;
          index2 = index2->next;
        }
        return index2;
      }
    }
    return nullptr;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [3,2,0,-4]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n0\n
// @lcpr case=end

// @lcpr case=start
// [1]\n-1\n
// @lcpr case=end

 */

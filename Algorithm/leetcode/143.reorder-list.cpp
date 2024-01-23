/*
 * @lc app=leetcode.cn id=143 lang=cpp
 * @lcpr version=30113
 *
 * [143] 重排链表
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
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};
// @lcpr-template-end
// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
 public:
  void reorderList(ListNode* head) {
    deque<ListNode*> dq;
    ListNode* cur = head;
    while (cur) {
      dq.push_back(cur);
      cur = cur->next;
    }
    cur = head;
    bool odd = true;
    ListNode* node = nullptr;
    while (dq.size()) {
      if (odd) {
        node = dq.front();
        dq.pop_front();
      } else {
        node = dq.back();
        dq.pop_back();
      }
      odd = !odd;
      cur->next = node;
      cur = cur->next;
    }
    cur->next = nullptr;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3,4]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

 */

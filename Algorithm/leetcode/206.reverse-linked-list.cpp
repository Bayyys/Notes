/*
 * @lc app=leetcode.cn id=206 lang=cpp
 * @lcpr version=30110
 *
 * [206] 反转链表
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
  ListNode* reverseList_stack(ListNode* head) {
    if (head == nullptr || head->next == nullptr) return head;
    stack<ListNode*> s = stack<ListNode*>();
    ListNode* curr = head;
    while (curr) {
      s.push(curr);
      curr = curr->next;
    }
    ListNode* pHead = new ListNode(0);
    curr = pHead;
    while (!s.empty()) {
      ListNode* tmp = s.top();
      s.pop();
      curr->next = tmp;
      curr = tmp;
    }
    curr->next = nullptr;
    return pHead->next;
  }

  ListNode* reverseList(ListNode* head) {
    ListNode* pHead = new ListNode(0);
    pHead->next = nullptr;
    ListNode* curr = head;
    while (curr) {
      ListNode* tmp = curr->next;
      curr->next = pHead->next;
      pHead->next = curr;
      curr = tmp;
    }
    return pHead->next;
  }

  ListNode* reverseList_recursion2(ListNode* head) {
    if (head == nullptr || head->next == nullptr) return head;  // 0 or 1 node
    ListNode* new_head = reverseList(head->next);
    head->next->next = head;
    head->next = nullptr;
    return new_head;
  }

  ListNode* reverseList_doublePoint(ListNode* head) {
    ListNode *first = head, *second = nullptr;
    ListNode* tmp = nullptr;
    while (first) {
      tmp = first->next;
      first->next = second;
      second = first;
      first = tmp;
    }
    return second;
  }

  ListNode* reverseList_recursion(ListNode* head) {
    return myReverse(NULL, head);
  }
  ListNode* myReverse(ListNode* prev, ListNode* curr) {
    if (curr == NULL) return prev;
    ListNode* tmp = curr->next;
    curr->next = prev;
    return myReverse(curr, tmp);
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

 */

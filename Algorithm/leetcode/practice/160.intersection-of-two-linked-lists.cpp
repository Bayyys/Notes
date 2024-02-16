// @lcpr-before-debug-begin

// @lcpr-before-debug-end

/*
 * @lc app=leetcode.cn id=160 lang=cpp
 * @lcpr version=30109
 *
 * [160] 相交链表
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
  ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    ListNode *pA = headA;
    ListNode *pB = headB;
    int lenA = 0, lenB = 0;
    while (pA || pB) {
      if (pA) {
        pA = pA->next;
        lenA++;
      }
      if (pB) {
        pB = pB->next;
        lenB++;
      }
    }
    int diffLen = abs(lenA - lenB);
    if (lenA < lenB) {
      ListNode *tmp = headA;
      int tmpLen = lenA;
      pA = headB;
      lenA = lenB;
      pB = headA;
      lenB = tmpLen;
    } else {
      pA = headA;
      pB = headB;
    }
    while (diffLen != 0) {
      pA = pA->next;
      diffLen--;
    }
    ListNode *res = nullptr;
    while (pA && pB) {
      if (pA == pB) {
        res = pA;
        break;
      }
      pA = pA->next;
      pB = pB->next;
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
// @lcpr case=end

// @lcpr case=start
// 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
// @lcpr case=end

// @lcpr case=start
// 0\n[2,6,4]\n[1,5]\n3\n2\n
// @lcpr case=end

 */

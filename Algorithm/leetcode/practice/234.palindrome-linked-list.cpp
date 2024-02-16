/*
 * @lc app=leetcode.cn id=234 lang=cpp
 * @lcpr version=30113
 *
 * [234] 回文链表
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
  bool isPalindrome(ListNode *head) {
    ListNode *cur = head;
    int len = 0;
    while (cur) {
      len++;
      cur = cur->next;
    }
    vector<int> vec(len, 0);
    cur = head;
    int index = 0;
    while (cur) {
      vec[index++] = cur->val;
      cur = cur->next;
    }
    int left = 0, right = len - 1;
    while (left < right) {
      if (vec[left] != vec[right]) return false;
      left++;
      right--;
    }
    return true;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [1,2,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n
// @lcpr case=end

 */

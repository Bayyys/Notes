#include <cassert>
#include <cstring>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *createList(const vector<int> &nums) {
  ListNode *head = nullptr;
  ListNode *tail = nullptr;
  for (auto num : nums) {
    ListNode *node = new ListNode(num);
    if (head == nullptr) {
      head = node;
      tail = node;
    } else {
      tail->next = node;
      tail = node;
    }
  }
  return head;
}

void printList(ListNode *head) {
  while (head != nullptr) {
    cout << head->val << " ";
    head = head->next;
  }
  cout << endl;
}

class Solution {
 public:
  ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    ListNode *eheadA = new ListNode(0), *eheadB = new ListNode(0);
    ListNode *longHead = new ListNode(0), *shortHead = new ListNode(0);
    eheadA->next = headA;
    eheadB->next = headB;
    int skip = 0;
    while (headA != nullptr && headB != nullptr) {
      headA = headA->next;
      headB = headB->next;
      skip++;
    }
    int Lshort = skip;
    ListNode *tmp = new ListNode(0);
    if (headA == nullptr) {
      longHead = eheadB;
      shortHead = eheadA;
      tmp = headB;
    } else {
      longHead = eheadA;
      shortHead = eheadB;
      tmp = headA;
    }
    while (tmp != nullptr) {
      tmp = tmp->next;
      skip++;
    }
    int Llong = skip;
    int gap = Llong - Lshort;
    while (gap--) {
      longHead = longHead->next;
    }
    while (longHead != nullptr) {
      if (longHead == shortHead) {
        return longHead;
      }
      longHead = longHead->next;
      shortHead = shortHead->next;
    }
    return nullptr;
  }
};

int main() {
  Solution so;
  ListNode *ans = so.getIntersectionNode(createList(vector<int>{
                                             1,
                                             2,
                                             3,
                                             4,
                                             5,
                                         }),
                                         createList(vector<int>{3, 4, 5}));
  printList(ans);
  cout << "hello world!" << endl;
  return 0;
}
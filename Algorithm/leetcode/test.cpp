#include <cassert>
#include <cstring>
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *createList(const vector<int> &nums)
{
    ListNode *head = nullptr;
    ListNode *tail = nullptr;
    for (auto num : nums)
    {
        ListNode *node = new ListNode(num);
        if (head == nullptr)
        {
            head = node;
            tail = node;
        }
        else
        {
            tail->next = node;
            tail = node;
        }
    }
    return head;
}

void printList(ListNode *head)
{
    while (head != nullptr)
    {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

class Solution
{
public:
    ListNode *reverse(ListNode *pred, ListNode *cur)
    {
        if(cur==nullptr)
            return pred;
        ListNode *tmp = cur->next;
        cur->next = pred;
        return reverse(cur, tmp);
    }
    ListNode *reverseList(ListNode *head)
    {
        return reverse(nullptr, head);
    }
};

int main()
{
    Solution so;
    vector<int> nums = {1, 2, 3};
    ListNode *head = createList(nums);
    ListNode *ans = so.reverseList(head);
    printList(ans);
    return 0;
}
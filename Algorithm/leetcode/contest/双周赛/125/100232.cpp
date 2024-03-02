#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class Solution {
 public:
  int minOperations(vector<int>& nums, int k) {
    // 定义一个优先级队列
    priority_queue<ll, vector<ll>, greater<ll>> pq;  // 队列弹出为最小值
    for (auto& n : nums) {
      pq.push(n);
    }
    int ans = 0;
    while (pq.top() < k) {
      ll a = pq.top();
      pq.pop();
      ll b = pq.top();
      pq.pop();
      pq.push(min(a, b) * 2 + max(a, b));
      ans++;
    }
    return ans;
  }
};

int main() {
  Solution s;
  vector<int> nums = {};
  return 0; }
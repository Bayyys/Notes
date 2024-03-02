#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class Solution {
 private:
  pair<int, int> check(int u, int v, int k) {
    long long sum = u + v;
    int u1 = u xor k;
    int v1 = v xor k;
    long long sum2 = u1 + v1;
    if (sum2 > sum) {
      return {u1, v1};
    } else {
      return {-1, -1};
    }
  }

 public:
  long long maximumValueSum(vector<int>& nums, int k,
                            vector<vector<int>>& edges) {
    int n = nums.size();
    stack<int> s;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        auto [u1, v1] = check(nums[i], nums[j], k);
        if (u1 != -1 && v1 != -1) {
          nums[i] = u1;
          nums[j] = v1;
          s.push(i), s.push(j);
        }
      }
    }
    while (!s.empty()) {
      int u = s.top();
      s.pop();
      for (int v = 0; v < n; v++) {
        if(u == v) continue;
        auto [u1, v1] = check(nums[u], nums[v], k);
        if (u1 != -1 && v1 != -1) {
          nums[u] = u1;
          nums[v] = v1;
          s.push(u), s.push(v);
        }
      }
    }
    return accumulate(nums.begin(), nums.end(), 0LL);
  }
};

int main() {
  Solution s;
  vector<int> nums = {24, 78, 1, 97, 44};
  int k = 6;
  vector<vector<int>> edges = {{0, 2}, {1, 2}, {4, 2}, {3, 4}};
  cout << s.maximumValueSum(nums, k, edges) << endl;
  return 0;
}
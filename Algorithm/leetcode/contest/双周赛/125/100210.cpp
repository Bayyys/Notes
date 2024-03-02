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
    cout << u << " " << v << " " << u1 << " " << v1 << " " << sum << " " << sum2 << endl;
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
    vector<vector<int>> g(n);
    long long sum = 0;
    for (auto& e : edges) {
      g[e[0]].push_back({e[1]});
      g[e[1]].push_back({e[0]});
    }
    stack<int> s;
    for (int u = 0; u < n; u++) {
      for (auto& v : g[u]) {
        int u0 = nums[u], v0 = nums[v];
        auto [u1, v1] = check(u0, v0, k);
        if (u1 != -1 && v1 != -1) {
          nums[u] = u1;
          nums[v] = v1;
          s.push(u), s.push(v);
        }
      }
    }
    while (!s.empty()) {
      int u = s.top();
      s.pop();
      for (auto& v : g[u]) {
        int u0 = nums[u], v0 = nums[v];
        auto [u1, v1] = check(u0, v0, k);
        if (u1 != -1 && v1 != -1) {
          nums[u] = u1;
          nums[v] = v1;
          s.push(u), s.push(v);
        }
      }
    }
    for(auto& num: nums) {
      sum += num;
    }
    return sum;
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
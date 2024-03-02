#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

inline void solve() {}

class Solution {
 public:
  int minOperations(vector<int>& nums, int k) {
    int ans = 0;
    for(auto &n: nums) {
      if (n < k) ans++;
    }
    return ans;
  }
};

int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<int> coins = {1, 3, 6, 10, 15};

inline void solve() {
  ll n = 0;  // [1, 1e9]
  int ans = 0;
  vector<int> c_cnt = {0, 0, 0, 0, 0};
  cin >> n;
  for (int i = coins.size() - 1; i >= 0; i--) {
    int c = n / coins[i];
    c_cnt[i] += c;
    n -= c * coins[i];
    ans += c;
  }
  while (c_cnt[0] >= 2 && c_cnt[1] >= 1 & c_cnt[4] >= 1) {
    c_cnt[0] -= 2;
    c_cnt[1] -= 1;
    c_cnt[3] += 2;
    c_cnt[4] -= 1;
    ans -= 2;
  }
  while (c_cnt[0] >= 2 && c_cnt[2] >= 1 & c_cnt[4] >= 1) {
    c_cnt[0] -= 2;
    c_cnt[2] -= 1;
    c_cnt[3] += 2;
    c_cnt[1] += 1;
    c_cnt[4] -= 1;
    ans -= 1;
  }
  while (c_cnt[0] >= 2 && c_cnt[3] >= 1) {
    c_cnt[0] -= 2;
    c_cnt[3] -= 1;
    c_cnt[2] += 2;
    ans -= 1;
  }
  cout << ans << endl;
}

int main() {
  int t = 0;
  cin >> t;
  while (t--) solve();

  return 0;
}
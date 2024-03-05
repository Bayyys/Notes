#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

inline void solve() {
  int n;
  ll c;
  cin >> n >> c;
  vector<int> a;
  for (register int i = 0; i < n; i++) {
    int x;
    cin >> x;
    a.emplace_back(x);
  }
  ll ans = ((c + 1) + (c % 2 == 0 ? 1 : 2)) * (c / 2 + 1) / 2;
  sort(a.begin(), a.end(), less<int>());
  n = a.size();
  for (register int i = n - 1; i >= 0; i--) {
    int cnt = a[i] / 2 + 1;  // 和为i的组合数
    cout << a[i] << cnt << " ";
    if (a[i] <= c / 2) {
      cnt += (c - a[i]);  // 差为i的组合数
    }
    cout << cnt << " ";
    cnt -= i;
    cout << cnt << endl;
    ans -= cnt;
  }
  cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
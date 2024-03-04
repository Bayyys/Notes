#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

inline void solve() {
  int n;
  cin >> n;
  vector<int> a, b;
  ll sum = 0;
  for (register int i = 0; i < n; i++) {
    int x;
    cin >> x;
    a.emplace_back(x);
  }
  for (register int i = 0; i < n; i++) {
    int x;
    cin >> x;
    b.emplace_back(x);
    sum += abs(x - a[i]);
  }
  int l = INT_MAX, r = 0;
  for (register int i = 0; i < n; i++) {
    l = min(l, max(a[i], b[i]));
    r = max(r, min(a[i], b[i]));
  }
  cout << sum + ((r - l) > 0 ? 2 * (r - l) : 0) << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
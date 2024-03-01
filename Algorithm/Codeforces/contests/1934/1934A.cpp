#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

inline void solve() {
  int n = 0;  // 数组长度 [4, 100]
  cin >> n;
  vector<int> a;
  for (register int i = 0; i < n; i++) {
    int x = 0;  // 数组元素 [-1e6, 1e6]
    cin >> x;
    a.emplace_back(x);
  }
  sort(a.begin(), a.end());
  int ans =
      a[n - 1] - a[0] + a[n - 1] - a[1] + a[n - 2] - a[0] + a[n - 2] - a[1];
  cout << ans << endl;
}

int main() {
  int t = 0;
  cin >> t;
  while (t--) solve();
  return 0;
}
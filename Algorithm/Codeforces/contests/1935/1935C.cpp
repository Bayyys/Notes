#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

inline void solve() {
  int n;  // 消息数量 [1, 2000]
  int l;  // 用户愿意在消息中花费的时间 [1, 1e9]
  cin >> n >> l;
  vector<int> a, b;
  for (register int i = 0; i < n; i++) {
    int x = 0, y = 0;
    cin >> x >> y;
    if (x > l) continue;
    a.emplace_back(x);
    b.emplace_back(y);
  }
  n = a.size();
  if (n == 0) {
    cout << 0 << endl;
    return;
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
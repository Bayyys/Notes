#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

inline void solve() {
  int n;  // 整数数量 [2, 1e5]
  cin >> n;
  vector<int> vis(n, 0);  // 记录是否访问过
  vector<int> a(n);
  for (register int i = 0; i < n; i++) {
    int x = 0;
    cin >> x;  // [0, n)
    a[i] = x;
    vis[x] = 1;
  }
  int mex = -1;
  for (register int i = 0; i < n; i++) {
    if (vis[i] == 0) {
      mex = i;
      break;
    }
  }
  if (mex == -1) {
    mex = n;
  }
  int cnt = 0;
  vector<int> vis2(mex, 0);
  int start = 1, end = 1;
  vector<pair<int, int>> ans;
  for (register int i = 0; i < n; i++) {
    if (a[i] < mex) {
      if (vis2[a[i]] == 0) {
        vis2[a[i]] = 1;
        cnt++;
      }
    }
    if (cnt == mex) {
      end = i + 1;
      cnt = 0;
      ans.push_back({start, end});
      fill(vis2.begin(), vis2.end(), 0);
      start = end + 1;
    }
  }
  // 将vis2最后一个对象的second幅值为n
  if (end < n) {
    ans.back().second = n;
  }
  if (ans.size() < 2) {
    cout << -1 << endl;
  } else {
    cout << ans.size() << endl;
    for (auto p : ans) {
      cout << p.first << " " << p.second << endl;
    }
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
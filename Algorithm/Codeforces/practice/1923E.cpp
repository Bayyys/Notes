// Count Paths
// https://codeforces.com/problemset/problem/1923/E
#include <bits/stdc++.h>
using namespace std;
#define fio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;

inline int read() {
  int s = 0;
  char ch = getchar();
  while (ch > '9' || ch < '0') ch = getchar();
  while (ch <= '9' && ch >= '0') {
    s = (s << 3) + (s << 1) + (ch ^ 48);
    ch = getchar();
  }
  return s;
}

inline void solve() {
  int n = read();                   // 点数  [2, 2*1e5]
  vector<int> col(n + 1);           // 颜色
  vector<vector<int>> path(n + 1);  // 路径
  vector<int> cnt(n + 1);           // 每个颜色的数量
  ll ans = 0;                       // 答案
  for (register int i = 1; i <= n; i++) {
    int x;
    x = read();
    col[i] = x;
  }
  for (register int i = 1; i < n; i++) {
    int x, y;
    x = read();
    y = read();
    path[x].emplace_back(y);
    path[y].emplace_back(x);
  }

  auto dfs = [&](auto f, int node, int father) -> void {
    int cur = cnt[col[node]];
    for (auto v : path[node]) {
      if (v == father) continue;
      cnt[col[node]] = 1;
      f(f, v, node);
    }
    ans += cur, cnt[col[node]] = cur + 1;
  };

  // 依次从每个节点开始遍历
  dfs(dfs, 1, 0);
  cout << ans << endl;
}

int main() {
  fio;
  int n = read();
  while (n--) {
    solve();
  }
  return 0;
}
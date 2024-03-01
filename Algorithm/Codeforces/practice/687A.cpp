// A. NP-Hard Problem
// https://codeforces.com/problemset/problem/687/A
#include <bits/stdc++.h>
using namespace std;
#define fio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;
int flag = 0;
vector<int> A, B;

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

inline void dfs(vector<vector<int>>& g, vector<int>& vis, vector<int>& color,
                int u, int c) {
  vis[u] = 1;
  color[u] = c;
  c == 1 ? A.push_back(u) : B.push_back(u);
  for (int v : g[u]) {
    if (!vis[v]) {
      dfs(g, vis, color, v, c == 1 ? 2 : 1);
    } else if (color[v] == color[u]) {
      flag = 1;
      return;
    }
  }
}

inline void write(vector<int>& v) {
  cout << v.size() << endl;
  for (auto& x : v) {
    cout << x << " ";
  }
  cout << endl;
}

inline void solve() {
  int n = read();  // 定点数 [2, 1e5]
  int m = read();  // 边数 [1, 1e5]
  vector<vector<int>> g(n + 1);
  vector<int> vis(n + 1, 0);
  vector<int> color(n + 1, 0);
  // 读入边
  for (register int i = 0; i < m; i++) {
    int u = read(), v = read();
    g[u].push_back(v), g[v].push_back(u);
  }
  // 填充颜色
  for (int i = 1; i <= n; i++) {
    if (flag == 1) break;
    if (!vis[i]) {
      if (g[i].empty()) continue;
      dfs(g, vis, color, i, 1);
    }
  }
  // 输出
  if (flag == 1) {
    cout << -1 << endl;
  } else {
    write(A);
    write(B);
  }
}

int main() {
  fio;
  solve();
  return 0;
}
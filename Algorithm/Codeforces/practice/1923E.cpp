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

void dfs(vector<int> &col, vector<vector<int>> &path, vector<int> &vis,
         int from) {
  // 递归遍历
  cout << from << endl;
  for (auto to : path[from]) {
    if (vis[to]) continue;
    vis[to] = 1;
    dfs(col, path, vis, to);
    vis[to] = 0;
  }
}

inline void solve() {
  int n = read();
  vector<int> col(1 + n);
  for (register int i = 1; i <= n; i++) col[i] = read();  // 读取颜色
  vector<vector<int>> path(n + 1);                        // 路径
  for (register int i = 1; i < n; i++) {
    int x, y;
    x = read(), y = read();
    path[x].emplace_back(y);
    path[y].emplace_back(x);
  }

  // 依次从每个节点开始遍历
  for (register int i = 1; i <= n; i++) {
    vector<int> vis(n + 1, 0);
    vis[i] = 1;  // 标记已访问
    dfs(col, path, vis, i);
    cout << "----" << endl;
  }
  cout << "====" << endl;
}

int main() {
  fio;
  int n = read();
  while (n--) {
    solve();
  }
  return 0;
}
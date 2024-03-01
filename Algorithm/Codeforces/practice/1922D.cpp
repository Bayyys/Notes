// Berserk Monsters
// https://codeforces.com/problemset/problem/1922/D
#include <bits/stdc++.h>
using namespace std;
#define fio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;

struct AckNode {
  ll a = 0, d = 0;
  ll r = -1, l = -1;
  AckNode() {}
  AckNode(int l, int r) : l(l), r(r), a(0), d(0) {}
};

void solve() {
  // 读入数据
  int n;
  cin >> n;
  vector<AckNode> v = vector<AckNode>(n + 5);  // 存储每个节点的数据
  for (int i = 1; i <= n; i++) cin >> v[i].a, v[i].r = i + 1, v[i].l = i - 1;
  for (int i = 1; i <= n; i++)
    cin >> v[i].d;  // 不存在的节点, v[i].r = -1, v[i].l = -1
  if (n == 1) {
    cout << "0\n";
    return;
  }

  auto get_dm = [&](int x) -> ll {
    ll res = 0;
    if (v[x].l != -1) res += v[v[x].l].a;
    if (v[x].r != -1) res += v[v[x].r].a;
    return res;
  };

  vector<int> ans(n, 0);          // 结果数组
  int cnt = 0;                    // 记录每轮次死亡的节点数
  vector<int> dead;               // 存储每轮次死亡的节点
  vector<int> visited(n + 2, 1);  // 记录每个节点是否存活
  for (int i = 1; i <= n; i++) {
    ll damage = get_dm(i);
    if (damage > v[i].d) dead.push_back(i);
  }

  for (int i = 0; i < n; i++) {  // 模拟n次攻击过程
    ans[i] = dead.size();
    if (i == n - 1) break;
    set<int> upd;  // 需要更新的节点
    for (auto x : dead) {
      visited[x] = 0;
      if (v[x].l != -1) v[v[x].l].r = v[x].r, upd.insert(v[x].l);
      if (v[x].r != -1) v[v[x].r].l = v[x].l, upd.insert(v[x].r);
    }
    dead.clear();
    for (auto x : upd) {
      if (visited[x] == 0 || v[x].l == -1 || v[x].r == -1) continue;
      ll damage = get_dm(x);
      if (damage > v[x].d) dead.push_back(x);
    }
  }

  // 输出结果
  for (int i = 0; i < n; i++) {
    cout << ans[i] << " ";
  }
  cout << '\n';
}

int main() {
  fio;

  int num;
  cin >> num;
  while (num--) solve();
  return 0;
}
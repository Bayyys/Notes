#include <bits/stdc++.h>
using namespace std;
#define fio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;

struct AckNode {
  ll a = 0, d = 0;
  ll r = 0, l = 0;
  ll damage = 0;
  AckNode() {}
  AckNode(int l, int r) : l(l), r(r), a(0), d(0) {}
};

void solve() {
  // 读入数据
  int n;
  cin >> n;
  vector<AckNode> v = vector<AckNode>(n + 5);
  for (int i = 1; i <= n; i++) cin >> v[i].a, v[i].r = i + 1, v[i].l = i - 1;
  for (int i = 1; i <= n; i++) cin >> v[i].d;

  // 结果数组
  vector<int> ans;
  int cnt = 0;
  set<int> s;
  vector<int> dis;
  vector<int> visited(n + 2, 1);
  for (int i = 1; i <= n; i++) s.insert(i);  // 首轮次, 全部进行模拟攻击
  // 其余轮次, 只死亡节点附近的节点进行模拟攻击

  for (int i = 1; i <= n; i++) {  // 模拟n次攻击
    cnt = 0;
    dis.clear();
    for (auto i : s) {
      dis.push_back(i);
    }
    s.clear();
    for (auto i : dis) {
      v[i].damage = v[i].d - v[v[i].l].a - v[v[i].r].a;
      if (v[i].damage < 0 && visited[i] == 1) {
        visited[i] = 0;
        if (v[i].l > 0) {
          s.insert(v[i].l);
        }
        v[v[i].l].r = v[i].r;
        if (v[i].r < n + 1) {
          s.insert(v[i].r);
        }
        v[v[i].r].l = v[i].l;
        cnt++;
      }
    }
    ans.push_back(cnt);
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
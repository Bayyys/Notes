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

const int N = 1e7 + 5;
vector<int> v(1e7 + 5);
int prime[N], ans[N];
ll d[N] = {0};
int vis[N] = {0};

inline ll sum(int x) {
  int res = 0;
  for (int i = 1; i * i <= x; i++) {
    if (x % i == 0) {
      res += i;
      if (i * i != x) res += x / i;
    }
  }
  return res;
}

inline void init(int n) {
  d[1] = 1;
  int cnt = 0;
  for (int i = 2; i <= n; i++) {
    if (!v[i]) prime[++cnt] = i, d[i] = 1 + prime[cnt];
    for (int j = 1; j <= cnt && prime[j] * i <= n; j++) {
      v[prime[j] * i] = 1;
      if (i % prime[j] == 0) {
        int x = prime[j] * i, s = 1;
        while (x % prime[j] == 0) x /= prime[j], s *= prime[j];
        d[i * prime[j]] = d[x] * sum(s);
        if (d[i * prime[j]] < 0 || d[i * prime[j]] > N) d[i * prime[j]] = 0;
        break;
      } else {
        d[i * prime[j]] = d[i] * d[prime[j]];
      }
      if (d[i * prime[j]] < 0 || d[i * prime[j]] > N) d[i * prime[j]] = 0;
    }
  }
  for (int i = 1; i <= n; i++) {
    if (ans[d[i]] == 0) ans[d[i]] = i;
  }
}

inline void solve() {
  int c = read();  // d(n) = c  [1, 1e7] 找到满足条件的最小n
  if (ans[c] == 0)
    cout << -1 << endl;
  else
    cout << ans[c] << endl;
}

int main() {
  fio;
  init(N);
  int t = read();  // 测试用例数 [1, 1e4]
  while (t--) solve();
  return 0;
}
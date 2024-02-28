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
  ll r = read(), b = read(), k = read();  // [1, 1e9]
  ll g = __gcd(r, b);
  r /= g, b /= g;
  if (r > b) swap(r, b);
  if ((k - 1) * r + 1 >= b)
    cout << "OBEY\n";
  else
    cout << "REBEL\n";
}

int main() {
  fio;
  int T = read();  // [1, 1000] 测试用例数量
  while (T--) solve();
  return 0;
}
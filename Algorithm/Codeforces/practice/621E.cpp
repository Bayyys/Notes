#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1e9 + 7;

vector<vector<ll>> M_mul(vector<vector<ll>> &A, vector<vector<ll>> &B,
                         int mod) {
  int n = A.size();
  vector<vector<ll>> ans(n, vector<ll>(n, 0));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      for (int k = 0; k < n; k++) {
        ans[i][j] = (ans[i][j] + A[i][k] * B[k][j]) % mod;
      }
    }
  }
  return ans;
}

vector<vector<ll>> M_pow(vector<vector<ll>> &A, int pow, ll mod) {
  int n = A.size();
  vector<vector<ll>> ans(n, vector<ll>(n, 0));
  for (int i = 0; i < n; i++) ans[i][i] = 1;
  while (pow) {
    if (pow % 2) ans = M_mul(ans, A, mod);
    A = M_mul(A, A, mod);
    pow >>= 1;
  }
  return ans;
}

inline void solve() {
  int n;  // 块中的数字数 [2, 50000]
  int b;  // 块数 [1, 1e9]
  int k;  // 余数 [0, 100]
  int x;  // 模数 [0, 100]
  cin >> n >> b >> k >> x;
  // 找到组合数 使得 num % x == k
  vector<ll> cnt(10, 0);  // 个数统计
  vector<ll> m(101, 0);   // 余数为 i 的个数
  m[0] = 1;               // 余数为 0 的个数为 1
  for (register int i = 0; i < n; i++) {
    int a;
    cin >> a;
    cnt[a]++;
  }
  vector<vector<ll>> A(x, vector<ll>(x, 0));
  for (int i = 0; i < x; i++) {
    for (int j = 1; j <= 9; j++) {
      A[i][(i * 10 + j) % x] += cnt[j];
    }
  }
  A = M_pow(A, b, MOD);
  cout << A[0][k] << endl;
}

int main() {
  solve();
  return 0;
}
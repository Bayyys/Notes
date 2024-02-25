#include <bits/stdc++.h>
#define fio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
#define int long long
using namespace std;
const int MOD = 1e9 + 7;

// len = 2^0 + 2^1 + 2^2 + ... + 2^(i-1) + c
//        奇    偶    奇           奇/偶

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

int com_sum(int n, bool is_odd) {  // 计算前n个奇数/偶数的和
  if (is_odd)
    return n * n % MOD;  // 奇数
  else
    return n * (n + 1) % MOD;  // 偶数
}

int com_n_font_sum(int n) {  // 计算前n个数的和
  int res = 0;               // 前n个数的和
  int tmp = 1, cnt = 0,
      odd_flag = 1;  // tmp: 2^i, cnt: 已经计算的个数, odd_flag: 奇偶标记
  int odd = 0, even = 0;  // 奇数/偶数序列的个数

  // 计算奇数/偶数序列的个数
  while (cnt + tmp <= n) {
    cnt += tmp;
    if (odd_flag)
      odd += tmp;
    else
      even += tmp;
    odd_flag ^= 1;
    tmp <<= 1;
  }

  // 计算剩余的个数
  if (odd_flag)
    odd += n - cnt;
  else
    even += n - cnt;

  odd %= MOD, even %= MOD;

  res = (com_sum(odd, 1) + com_sum(even, 0)) % MOD;
  return res % MOD;
}

void solve(int l, int r) {
  cout << (com_n_font_sum(r) - com_n_font_sum(l - 1) + MOD) % MOD << endl;
}

signed main() {
  fio;
  int l = read(), r = read();
  solve(l, r);
  return 0;
}
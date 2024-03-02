#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
const ll MOD = 1e9 + 7;

inline ll cal(ll x, ll a) {
  ll ans = 1;
  while (a) {
    if (a & 1) ans = ans * x % MOD;
    x = x * x % MOD;
    a >>= 1;
  }
  return ans;
}

int main() {
  cin >> n;
  cout << (cal(3, 3 * n) - cal(7, n) + MOD) % MOD << endl;
  return 0;
}
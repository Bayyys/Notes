#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// 给定一个整数变量 x, 初始值为 n. 单次中断操作由以下步骤组成：
// 1. 选择一个值 y, 使得 0<y<x 和 0<(x⊕y)<x .
// 2. 通过设置 x=y 或设置 x=x⊕y 更新 x
// 确定是否可以使用最多 63 次中断操作, 将 x 转换为 m。 如果是, 请提供实现 x=m
// 所需的操作序列

inline void solve() {
  ll x, m;  // [1, 1e18]
  cin >> x >> m;
  ll y = x;
  int round = 0;
  int max_round = 64;
  vector<ll> ans;
  while (x != m && max_round--) {
    if (x < m) {
      x = x ^ (x + 1);
    } else {
      x = x ^ (x - 1);
    }
    ans.emplace_back(x);
    round++;
  }
  if (x == m) {
    cout << round - 1 << endl;
    cout << y << " ";
    for (auto &i : ans) {
      cout << i << " ";
    }
    cout << endl;
  } else {
    cout << -1 << endl;
  }
}

int main() {
  int t = 0;
  cin >> t;
  while (t--) solve();
  return 0;
}
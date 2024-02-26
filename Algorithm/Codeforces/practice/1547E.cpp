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
  /*数据读取*/
  int n = read(), k = read();     // 房间数[1, 3e5], 空调数[1, n]
  vector<pair<int, int>> con(k);  // con{位置, 温度} = con{ai, ti}
  // 空调位置 ai
  for (register int i = 0; i < k; i++) {
    con[i].first = read();
  }
  // 制冷温度 ti
  for (register int i = 0; i < k; i++) {
    con[i].second = read();
  }

  /*数据处理*/

  /* 1. 暴力搜索 */
  // for (register int i = 0; i < n; i++) {
  //   int minn = INT_MAX;
  //   for (auto &j : con) {
  //     minn = min(minn, abs(i + 1 - j.first) + j.second);
  //   }
  //   cout << minn << " ";
  // }

  /* 2. 优化搜索 */
  // 每一个空调位置向左/向右依次-1  {..., 17, 16, 15, 14, 15, 16, 17, ...}
  // 每一个格子是左右两个空调位置的最小值+1
  vector<int> temp(n, 0x3f3f3f3f);  // 房间温度
  for (register int i = 0; i < k; i++) {
    temp[con[i].first - 1] = con[i].second;
  }
  for (register int i = 1; i < n; i++) temp[i] = min(temp[i], temp[i - 1] + 1);
  for (register int i = n - 2; i >= 0; i--)
    temp[i] = min(temp[i], temp[i + 1] + 1);
  for (auto &i : temp) cout << i << " ";
  cout << endl;
}

int main() {
  fio;
  int q = read();
  while (q--) {
    solve();
  }

  return 0;
}
// Three Religions
// https://codeforces.com/problemset/problem/1149/B
#include <bits/stdc++.h>
using namespace std;
#define fio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;

const int N = 1e5 + 5;
const int M = 255;

char op, c;      // 操作符, 插入字符
string s;        // 母串 len: n [1, 1e5]
int n, q;        // 字符串长度, 查询次数 [1, 1e3]
int idx = 0;     // 插入位置
int nxt[N][28];  // 26 个字母的下一个位置
int len[4];      // 三个字符串的长度
int str[4][M];   // 三个字符串的位置
int f[M][M][M];

void init() {
  for (int i = 0; i < 26; i++)
    nxt[n + 1][i] = nxt[n + 2][i] =
        n + 1;  // 初始化 nxt[n+1][i] = nxt[n+2][i] = n + 1
  for (int i = n; i; i--) {
    for (int j = 0; j < 26; j++) {
      if (s[i] == j + 'a')
        nxt[i][j] = i;
      else
        nxt[i][j] = nxt[i + 1][j];
    }
  }
}

inline void solve() {
  cin >> s;
  s = " " + s;

  // 处理 nxt 数组
  init();

  // for (int i = 0; i < n + 2; i++) {
  //   for (int j = 0; j < 26; j++) {
  //     cout << nxt[i][j] << " ";
  //   }
  //   cout << endl;
  // }

  // 循环问询
  while (q--) {
    cin >> op;
    cin >> idx;

    if (op == '+') {
      cin >> c;
      str[idx][++len[idx]] = c - 'a';  // 将对应字符串的字符插入

      for (int i = (idx == 1 ? len[1] : 0); i <= len[1]; i++) {
        for (int j = (idx == 2 ? len[2] : 0); j <= len[2]; j++) {
          for (int k = (idx == 3 ? len[3] : 0); k <= len[3]; k++) {
            int &now = f[i][j][k];
            now = n + 1;
            if (j) now = min(now, nxt[f[i][j - 1][k] + 1][str[2][j]]);
            if (k) now = min(now, nxt[f[i][j][k - 1] + 1][str[3][k]]);
            if (i) now = min(now, nxt[f[i - 1][j][k] + 1][str[1][i]]);
          }
        }
      }
    } else {
      len[idx]--;
    }
    if (f[len[1]][len[2]][len[3]] <= n)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
}

int main() {
  fio;
  cin >> n >> q;
  solve();
  return 0;
}
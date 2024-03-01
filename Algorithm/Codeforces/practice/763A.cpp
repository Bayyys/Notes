// A: Timofey and a tree
// https://codeforces.com/problemset/problem/763/A
#include <iostream>
#pragma GCC optimize("O3")

using namespace std;

const int MAX = 1e5 + 5;
int u[MAX], v[MAX], color[MAX];
int cnt[MAX];
int diff = 0;

int main() {
  int n;
  cin >> n;
  for (int i = 1; i < n; i++) cin >> u[i] >> v[i];
  for (int i = 1; i <= n; i++) cin >> color[i];
  for (int i = 1; i < n; i++) {
    if (color[u[i]] != color[v[i]]) {
      diff++;
      cnt[u[i]]++;
      cnt[v[i]]++;
    }
  }
  for (int i = 1; i <= n; i++) {
    if (diff == cnt[i]) {
        cout << "YES" << endl;
        cout << i << endl;
        return 0;
    }
  }
  cout << "NO" << endl;
  return 0;
}
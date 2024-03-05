#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool check(string s1, string s2) {
  int n = s1.size();
  for (register int i = 0; i < n; i++) {
    if (s1[i] == s2[i]) continue;
    if (s1[i] > s2[i])
      return false;
    else
      return true;
  }
  return true;
}

inline void solve() {
  int n;
  cin >> n;
  string str;
  cin >> str;
  string str2 = str;
  reverse(str2.begin(), str2.end());
  if (check(str, str2)) {
    // str 就是最小的字典序
    cout << str << endl;
  } else {
    cout << str2 << str << endl;
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
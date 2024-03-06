#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

inline void solve() {
  int n;  // number of all moves [0, 1e9]
  int k;  // number of the third type of moves [3, 1e9]
  cin >> n >> k;
  if (k % 3 != 0) {
    if (n % 3 == 0)
      cout << "Bob" << endl;
    else
      cout << "Alice" << endl;
  } else {
    n %= (k + 1);
    if (n % 3 == 0 && n != k) {
      cout << "Bob" << endl;
    } else {
      cout << "Alice" << endl;
    }
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
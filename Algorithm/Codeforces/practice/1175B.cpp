// Catch Overflow!
// https://codeforces.com/problemset/problem/1175/B
#include <bits/stdc++.h>
using namespace std;
#define fio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long int lli;
typedef long long ll;
const ll MAX = pow(2, 32);

void solve(int n) {
  stack<ll> s;  // 操作栈: 1) add -> 0 2) for n -> n
  s.push(1);    // 初始化栈
  // end -> 栈弹出
  ll val = 0;  // 当前的值
  while (n--) {
    string str;
    cin >> str;
    if (str == "for") {
      ll x;
      cin >> x;
      s.push(min(MAX, x * s.top()));
    } else if (str == "end") {
      s.pop();
    } else if (str == "add") {
      val += s.top();
    }
  }
  if (val >= MAX)
    cout << "OVERFLOW!!!" << endl;
  else
    cout << val << endl;
}

int main() {
  fio;
  int n;
  cin >> n;
  solve(n);
  return 0;
}
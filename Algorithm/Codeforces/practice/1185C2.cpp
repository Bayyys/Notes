#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

inline void solve() {
  int n, M;  // n: 学生数[1, 100], M: 考试时间总和[1, 100]
  cin >> n >> M;
  int sum = 0;
  priority_queue<int> q;
  priority_queue<int, vector<int>, greater<int>> q2;
  for (register int i = 0; i < n; i++) {
    int x;
    cin >> x;
    sum += x;
    while (!q.empty() && sum > M) {
      sum -= q.top();
      q2.push(q.top());
      q.pop();
    }
    if (!q.empty() && !q2.empty() && q.top() > q2.top()) {
      sum -= q.top();
      q2.push(q.top());
      q.pop();
    }
    while (!q2.empty() && sum + q2.top() <= M) {
      sum += q2.top();
      q.push(q2.top());
      q2.pop();
    }
    cout << q2.size() << " ";
    q.push(x);
  }
}

int main() {
  solve();
  return 0;
}
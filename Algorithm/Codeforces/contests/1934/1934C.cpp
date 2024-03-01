#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
vector<int> query_ans;

int ask(int x, int y) {
  cout << "? " << x << " " << y << endl;
  int res = 0;
  cin >> res;
  return res;
}

void write(int x, int y) { cout << "! " << x << " " << y << endl; }

int query(int x, int y, vector<vector<int>> &mines,
          vector<pair<int, int>> &points) {
  points.clear();
  int cnt = 0;
  int c0, c1;
  int answer = ask(x, y);
  query_ans.emplace_back(answer);
  if (answer == 0) {
    write(x, y);
    return 0;
  } else {
    mines[x][y] = 2;
    for (int row = -answer; row <= answer; row++) {
      for (int col = -answer; col <= answer; col++) {
        if (x + row > 0 && x + row < mines.size() && y + col > 0 &&
            y + col < mines[0].size()) {
          int x0 = x + row, y0 = y + col;
          int v = abs(row) + abs(col);
          if (v < answer) {
            mines[x0][y0] = 2;
          } else if (v == answer) {
            if (mines[x0][y0] == 0) {
              mines[x0][y0] = 1;
              if (cnt == 0) {
                c0 = x0, c1 = y0;
              }
              cnt++;
            } else if (mines[x0][y0] == 1) {
              mines[x0][y0] = 1;
              // 下一个寻找点
              points.emplace_back(x0, y0);
              if (cnt == 0) {
                c0 = x0, c1 = y0;
              }
              cnt++;
            }
          }
        }
      }
    }
  }
  if (cnt == 1) {
    write(c0, c1);
    return 0;
  } else {
    return -1;
  }
}

inline void solve() {
  int n, m;  // 行: [2, 1e8], 列: [2, 1e8]
  cin >> n >> m;
  vector<vector<int>> mines(
      n + 1, vector<int>(m + 1, 0));  // 0: 未访问, 1: 可能有雷1, 2: 无雷
  vector<pair<int, int>> points;
  int q;
  // 询问左上角
  q = query(1, 1, mines, points);
  if (q == 0) return;
  // 询问左下角
  q = query(n, 1, mines, points);
  if (q == 0) return;
  // 如果交点非空, 询问
  if (!points.empty()) {
    q = query(points[0].first, points[0].second, mines, points);
    if (q == 0) return;
    q = query(points[0].first, points[0].second, mines, points);
    if (q == 0)
      return;
    else {
      write(points[1].first, points[1].second);
      return;
    }
  } else {
    int p1 = 1 + query_ans[0], p2 = n - query_ans[1];
    q = query((p1 + p2) / 2, 1, mines, points);
    if (q == 0) return;
    q = query(points[0].first, points[0].second, mines, points);
    if (q == 0)
      return;
    else {
      write(points[1].first, points[1].second);
      return;
    }
  }
}

int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

inline void solve() {}

class Solution {
 public:
  vector<int> countPairsOfConnectableServers(vector<vector<int>>& edges,
                                             int signalSpeed) {
    int n = edges.size() + 1;
    vector<int> count(n, 0);
    vector<vector<pair<int, int>>> g(n);
    for (auto& e : edges) {
      int u = e[0], v = e[1], w = e[2];
      g[u].push_back({v, w});
      g[v].push_back({u, w});
    }
    vector<int> path;
    auto dfs = [&](auto&& f, int node, int parent, int value) -> int {
      int path_length = 0;
      for (auto [v, w] : g[node]) {
        if (v == parent) continue;
        if ((value + w) % signalSpeed == 0) {
          path_length++;
        }
        int l = f(f, v, node, value + w);
        path_length += l;
      }
      return path_length;
    };
    for (int i = 0; i < n; i++) {
      vector<int> path;
      for (auto [node, w] : g[i]) {
        int l = dfs(dfs, node, i, w);
        if (w % signalSpeed == 0) {
          l++;
        }
        if (l > 0) {
          path.push_back(l);
        }
      }
      if (path.size() <= 1) {
        continue;
      } else {
        int pl = 0;
        int n = path.size();
        for (int i = 0; i < n; i++) {
          for (int j = i + 1; j < n; j++) {
            pl += path[i] * path[j];
          }
        }
        count[i] = pl;
      }
    }
    return count;
  }
};

int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
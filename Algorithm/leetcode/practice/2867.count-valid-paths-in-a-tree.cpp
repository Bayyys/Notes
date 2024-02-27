/*
 * @lc app=leetcode.cn id=2867 lang=cpp
 * @lcpr version=30117
 *
 * [2867] 统计树中的合法路径数目
 */

// @lcpr-template-start
using namespace std;
#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

// @lcpr-template-end
// @lc code=start
const int N = 1e5 + 5;
class Solution {
 private:
  vector<bool> isPrimes = vector<bool>(N + 1, true);

  void init() {
    isPrimes[1] = false;
    for (int i = 2; i * i <= N; i++) {
      if (isPrimes[i]) {
        for (int j = i * i; j <= N; j += i) {
          isPrimes[j] = false;
        }
      }
    }
  }

  void dfs(const vector<vector<int>> &graph, vector<int> &nonPrimePath, int i,
           int pre) {
    // i: 当前节点; pre: 父节点
    nonPrimePath.push_back(i);
    for (auto j : graph[i]) {
      if (j == pre || isPrimes[j]) continue;  // 跳过父节点和质数节点
      dfs(graph, nonPrimePath, j, i);
    }
  }

 public:
  long long countPaths(int n, vector<vector<int>> &edges) {
    // 生成素数表
    init();
    // 构建图
    vector<vector<int>> graph(n + 1);
    for (auto &edge : edges) {
      graph[edge[0]].push_back(edge[1]);
      graph[edge[1]].push_back(edge[0]);
    }
    // 分别计算质数节点的合数子树的个数
    vector<int> nonPrimePath;
    long long res = 0;
    vector<long long> count(n + 1, 0);
    for (int i = 1; i <= n; i++) {
      if (!isPrimes[i]) continue;
      long long cur = 0;
      for (auto j : graph[i]) {
        if (isPrimes[j]) continue;
        if (count[j] == 0) {     // 未计算过
          nonPrimePath.clear();  // 清空路径
          dfs(graph, nonPrimePath, j, 0);
          long long cnt = nonPrimePath.size();
          for (auto k : nonPrimePath) {
            count[k] = cnt;
          }
        }
        res += count[j] * cur;
        cur += count[j];
      }
      res += cur;
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// 5\n[[1,2],[1,3],[2,4],[2,5]]\n
// @lcpr case=end

// @lcpr case=start
// 6\n[[1,2],[1,3],[2,4],[3,5],[3,6]]\n
// @lcpr case=end

 */

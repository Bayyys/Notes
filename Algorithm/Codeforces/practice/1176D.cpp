#include <bits/stdc++.h>
using namespace std;
#define fio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;
const int NB = 2750131;
const int MAX = 2e5 + 10;

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

int n;
vector<int> a, b;         // 输入数组 a[n] b[2n]
vector<int> prime(1, 1);  // 素数表
bool mark[NB] = {false};  // 非素数标记
bool vis[NB] = {false};   // 访问标记
int cnt[NB] = {0};        // 计数器

inline void init_prime(int num) {
  int cnt = 1;
  for (register int i = 2; i <= num; i++) {
    if (!mark[i]) prime.emplace_back(i), cnt++;
    for (register int j = 1; j <= cnt && i * prime[j] <= num; j++) {
      mark[i * prime[j]] = true;
      if (i % prime[j] == 0) break;
    }
  }
}

// 获取num的最小质因子
inline int get_nprime(int num) {
  if (num % 2 == 0) return num / 2;
  for (register int i = 3; i * i <= num; i += 2) {
    if (num % i == 0) return num / i;
  }
  return 0;
}

inline void readb() {
  for (register int i = 0; i < 2 * n; i++) {
    b.emplace_back(read());
  }
}

void solve() {
  sort(b.begin(), b.end());  // 从小到大排序
  // 从大到小找到b中的合数进行分析
  for (register int i = 2 * n - 1; i >= 0; i--) {
    if (!mark[b[i]]  // 是素数
        || vis[i])   // 已经被分析过
      continue;
    vis[i] = true, a.emplace_back(b[i]);  // 此合数一定为a中的元素
    int max_divisor = get_nprime(b[i]);   // 最大质因子
    int lindex = lower_bound(b.begin(), b.end(), max_divisor) - b.begin() +
                 cnt[max_divisor];  // 找到b中 max_divisor 的位置
    cnt[max_divisor]++;             // 计数器+1
    vis[lindex] = true;
  }

  // 从小到大找到b中的质数进行分析
  for (register int i = 0; i < 2 * n; i++) {
    if (vis[i])  // 已经被分析过(此时所有合数以及部分质数均被分析完)
      continue;
    vis[i] = true,
    a.emplace_back(b[i]);  // 此质数一定为a中的元素(质数只会生成更大的质数)
    int lindex = lower_bound(b.begin(), b.end(), prime[b[i]]) - b.begin() +
                 cnt[prime[b[i]]];  // 找到b中 prime[a[i]] 的位置
    cnt[prime[b[i]]]++;             // 计数器+1
    vis[lindex] = true;
  }
  for (auto i : a) cout << i << " ";
}

int main() {
  fio;
  n = read();
  init_prime(NB);
  readb();
  solve();
  return 0;
}
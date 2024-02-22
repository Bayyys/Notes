#include <bits/stdc++.h>
using namespace std;
#define fio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;

const int N = 1010;

ll s[N];
/**
 * @brief 询问函数
 *
 * @param t 询问类型: 1->三点构成三角形面积(△aiajak), 2-> 叉积(aiaj x aiak)
 * @param i, j, k 三点的编号
 * @return ll 询问结果(t=1->三角形面积; t=2->[-1: ])
 */
ll ask(ll t, ll i, ll j, ll k) {
  cout << t << " " << i << " " << j << " " << k << endl;
  ll res;
  cin >> res;
  return res;
}

bool cmp1(ll x, ll y) { return s[x] < s[y]; }  // 峰值点以前: 面积从小到大
bool cmp2(ll x, ll y) { return s[x] > s[y]; }  // 峰值点以后: 面积从大到小

void solve(int n) {
  ll first = 1, second = 2;
  // 1. 找到 1 的下一个点, ask(2, first, second, i) === 1
  for (ll i = 3; i <= n; i++)
    if (ask(2, first, second, i) == -1) second = i;

  // 2. 找到 a1a2 对应的峰值点: max(△a1a2ai); 记录每个点和a1a2构成三角形的面积
  ll amax = 0;
  for (ll i = 2; i <= n; i++) {
    if (i == second) continue;
    s[i] = ask(1, first, second, i);
    if (s[i] > s[amax]) amax = i;
  }

  // 3. 确定其他点的位置
  vector<ll> prear, pfront;
  for (ll i = 2; i <= n; i++) {
    if (i == second || i == amax) continue;
    ll res = ask(2, first, amax, i);
    if (res == 1)
      prear.push_back(i);
    else
      pfront.push_back(i);
  }

  // 4. 按照面积进行排序
  sort(pfront.begin(), pfront.end(), cmp1);
  sort(prear.begin(), prear.end(), cmp2);
  cout << "0 1 " << second << " ";
  for (auto x : pfront) cout << x << " ";
  cout << amax << " ";
  for (auto x : prear) cout << x << " ";
}

int main() {
  fio;
  int n;
  cin >> n;
  solve(n);
  return 0;
}
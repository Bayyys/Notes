#include <bits/stdc++.h>
using namespace std;

/* vector 版本 */
const int MAX = 2e5 + 10;

vector<int> prime(1, 1);
vector<bool> mark(MAX, false);

void init_prime(int num) {
  int cnt = 1;
  for (register int i = 2; i <= num; i++) {
    // 如果未标记则得到一个素数
    if (!mark[i]) prime.emplace_back(i), cnt++;
    // 标记目前得到的素数的i倍为非素数
    for (register int j = 1; j <= cnt && i * prime[j] <= num; j++) {
      mark[i * prime[j]] = true;
      if (i % prime[j] == 0) break;
    }
  }
}

/* 数组版本 */
const int MAXSIZE = 1e5 + 10;
int Mark[MAXSIZE], prime[MAXSIZE];

void Prime() {
  int index = 0;
  for (int i = 2; i < MAXSIZE; i++) {
    // 如果未标记则得到一个素数
    if (Mark[i] == 0) prime[++index] = i;
    // 标记目前得到的素数的i倍为非素数
    for (int j = 1; j <= index && prime[j] * i < MAXSIZE; j++) {
      Mark[i * prime[j]] = 1;
      if (i % prime[j] == 0) break;
    }
  }
}
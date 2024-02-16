/*
 * @lc app=leetcode.cn id=49 lang=cpp
 * @lcpr version=30110
 *
 * [49] 字母异位词分组
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
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
// @lcpr-template-end
// @lc code=start
class Solution {
 public:
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    vector<vector<string>> ans;

    /* 1.质数方法 (将每个字母映射到一个质数，字符串的乘积就是唯一的)
    vector<int> prime = getPrime();
    unordered_map<double, vector<string>> hash;
    for (auto str : strs) {
      double product = computePrimeProduct(str, prime);
      hash[product].push_back(str);
    }
    for (auto& [_, vec] : hash) {
      ans.push_back(vec);
    }
    */

    /* 2. 字母排序方法 (将每个字符串排序，排序后的字符串作为key) */
    unordered_map<string, vector<string>> mp;
    for (auto& str : strs) {
      string key = str;
      sort(key.begin(), key.end());
      mp[key].push_back(str);
    }
    for (auto& [_, vec] : mp) {
      ans.push_back(vec);
    }
    return ans;
  }

  //   // 计算字符串的质数乘积
  //   double computePrimeProduct(string& str, vector<int>& prime) {
  //     double product = 1;
  //     for (auto ch : str) {
  //       product *= prime[ch - 'a'];
  //     }
  //     return product;
  //   }

  //   // 得到顺序26个质数
  //   vector<int> getPrime() {
  //     vector<int> prime(26, 0);
  //     int cnt = 0;
  //     for (int i = 2; cnt < 26; i++) {
  //       bool isPrime = true;
  //       for (int j = 2; j * j <= i; j++) {
  //         if (i % j == 0) {  // 不是质数
  //           isPrime = false;
  //           break;
  //         }
  //       }
  //       if (isPrime) {
  //         prime[cnt++] = i;
  //       }
  //     }
  //     return prime;
  //   }
};
// @lc code=end

/*
// @lcpr case=start
// ["eat", "tea", "tan", "ate", "nat", "bat"]\n
// @lcpr case=end

// @lcpr case=start
// [""]\n
// @lcpr case=end

// @lcpr case=start
// ["a"]\n
// @lcpr case=end

 */

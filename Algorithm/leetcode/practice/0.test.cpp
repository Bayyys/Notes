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
#include <set>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
 private:
  void get_nextval(const string& pattern, vector<int>& nextval) {
    int j = 0, k = -1;  // k 表示前缀，j 表示后缀
    nextval[0] = -1;    // nextval[0] 初始化为 -1
    while (j < pattern.size() - 1) {
      if (k == -1 || pattern[j] == pattern[k]) {  // 当两个字符相等时要跳过
        j++;
        k++;
        nextval[j] = k;
      } else {
        k = nextval[k];
      }
    }
  }

 public:
  int countMatchingSubarrays(vector<int>& nums, vector<int>& pattern) {
    // 1. 根据 nums 和 pattern 分别构建 匹配字符串 和 模式串
    int res = 0;
    int n = nums.size(), m = pattern.size();
    string src, pat;
    for (int i = 0; i < n - 1; i++) {
      src.push_back(nums[i] == nums[i + 1]  ? '1'
                    : nums[i] < nums[i + 1] ? '2'
                                            : '0');
    }
    for (auto& p : pattern) {
      pat.push_back(p == 0 ? '1' : p == -1 ? '0' : '2');
    }
    vector<int> next(m);
    get_nextval(pat, next);
    for (int i = 0, j = 0; i < n - 1;) {
      if (j == -1 || src[i] == pat[j]) {
        i++;
        j++;
      } else {
        j = next[j];
      }
      if (j == m) {
        i--;
        res++;
        j = next[j - 1];
      }
    }
    return res;
  }
};

int main() {
  Solution sol;
  vector<int> nums = {1, 2, 3, 4, 5, 6};
  vector<int> pattern = {1, 1};
  int ans = sol.countMatchingSubarrays(nums, pattern);
  cout << ans << endl;
  return 0;
}
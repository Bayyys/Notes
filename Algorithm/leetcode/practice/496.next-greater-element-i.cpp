/*
 * @lc app=leetcode.cn id=496 lang=cpp
 * @lcpr version=30112
 *
 * [496] 下一个更大元素 I
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
  vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    stack<int> st;
    vector<int> res(nums1.size(), -1);
    if (nums1.size() == 0) return res;
    unordered_map<int, int> umap;  // key: nums1的值, value: nums1的索引
    for (int i = 0; i < nums1.size(); i++) umap[nums1[i]] = i;
    st.push(0);
    for (int i = 1; i < nums2.size(); i++) {
      while (!st.empty() && nums2[i] > nums2[st.top()]) {
        if (umap.count(nums2[st.top()])) {
          res[umap[nums2[st.top()]]] = nums2[i];
        }
        st.pop();
      }
      st.push(i);
    }
    return res;
  }
};
// @lc code=end

/*
// @lcpr case=start
// [4,1,2]\n[1,3,4,2].\n
// @lcpr case=end

// @lcpr case=start
// [2,4]\n[1,2,3,4].\n
// @lcpr case=end

 */

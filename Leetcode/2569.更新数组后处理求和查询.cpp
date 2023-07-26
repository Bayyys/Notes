/*
 * @lc app=leetcode.cn id=2569 lang=cpp
 *
 * [2569] 更新数组后处理求和查询
 *
 * https://leetcode.cn/problems/handling-sum-queries-after-update/description/
 *
 * algorithms
 * Hard (39.82%)
 * Likes:    32
 * Dislikes: 0
 * Total Accepted:    5.2K
 * Total Submissions: 12.1K
 * Testcase Example:  '[1,0,1]\n[0,0,0]\n[[1,1,1],[2,1,0],[3,0,0]]'
 *
 * 给你两个下标从 0 开始的数组 nums1
 * 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：
 *
 *
 * 操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标
 * r 的所有 0 反转成 1 或将 1 反转成 0 。l 和 r 下标都从 0 开始。 操作类型 2
 * 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i]
 * = nums2[i]
 * + nums1[i] * p 。
 * 操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
 *
 *
 * 请你返回一个数组，包含所有第三种操作类型的答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
 * 输出：[3]
 * 解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1]
 * ，所以第三个操作的答案为 3 。所以返回 [3] 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
 * 输出：[5]
 * 解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5
 * 。所以返回 [5] 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums1.length,nums2.length <= 10^5
 * nums1.length = nums2.length
 * 1 <= queries.length <= 10^5
 * queries[i].length = 3
 * 0 <= l <= r <= nums1.length - 1
 * 0 <= p <= 10^6
 * 0 <= nums1[i] <= 1
 * 0 <= nums2[i] <= 10^9
 *
 *
 */

// @lc code=start
#include <iostream>
#include <queue>
#include <vector>
class Solution {
 public:
  vector<long long> handleQuery(vector<int>& nums1, vector<int>& nums2,
                                vector<vector<int>>& queries) {
    vector<long long> q;
    for (int i = 0; i < queries.size(); i++) {
        vector<int> &query = queries[i];
        int type = query.front();
        if (type == 1) {
          int l = query[1];
          int r = query[2];
          for (int i = l; i <= r; i++) {
            nums1[i] = 1 - nums1[i];
          }
        } else if (type == 2) {
          int p = query[1];
          for (int i = 0; i < nums1.size(); i++) {
            nums2[i] += nums1[i] * p;
          }
        } else if (type == 3) {
          long long sum = 0;
          for (int i = 0; i < nums2.size(); i++) {
            sum += nums2[i];
          }
          q.push_back(sum);
        }
    }
    return q;
  }
};
// @lc code=end

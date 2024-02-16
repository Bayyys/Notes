/*
 * @lc app=leetcode.cn id=69 lang=cpp
 *
 * [69] x 的平方根
 *
 * https://leetcode.cn/problems/sqrtx/description/
 *
 * algorithms
 * Easy (38.41%)
 * Likes:    1390
 * Dislikes: 0
 * Total Accepted:    764.7K
 * Total Submissions: 2M
 * Testcase Example:  '4'
 *
 * 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
 *
 * 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
 *
 * 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：x = 4
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：x = 8
 * 输出：2
 * 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= x <= 2^31 - 1
 *
 *
 */

// @lc code=start
class Solution
{
public:
    int mySqrt(int x)
    {
        if (1 == x)
        {
            return 1;
        }
        int left = 1, right = x / 2;
        while (left <= right)
        {
            long long res = left + (right - left) / 2;
            if (res * res > x)
            {
                right = res - 1;
            }
            else if (res * res < x)
            {
                left = res + 1;
            }
            else
            {
                return res;
            }
        }
        return left < right ? left : right;
    }
};

// @lc code=end

/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode.cn/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (49.55%)
 * Likes:    1484
 * Dislikes: 0
 * Total Accepted:    403.5K
 * Total Submissions: 813.4K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,2,3,6,9,8,7,4,5]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == matrix.length
 * n == matrix[i].length
 * 1 
 * -100 
 * 
 * 
 */

// @lc code=start
class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        if (matrix.size() == 0)
        {
            return {};
        }
        vector<int> ans;
        int up = 0, down = matrix.size() - 1, left = 0, right = matrix[0].size() - 1;
        while (up <= down && left <= right)
        {
            if (up == down)
            {
                for (int i = left; i <= right; i++)
                {
                    ans.push_back(matrix[up][i]);
                }
                break;
            }
            else if (left == right)
            {
                for (int i = up; i <= down; i++)
                {
                    ans.push_back(matrix[i][left]);
                }
                break;
            }
            for (int i = left; i < right; i++)
            {
                ans.push_back(matrix[up][i]);
            }
            for (int i = up; i < down; i++)
            {
                ans.push_back(matrix[i][right]);
            }
            for (int i = right; i > left; i--)
            {
                ans.push_back(matrix[down][i]);
            }
            for (int i = down; i > up; i--)
            {
                ans.push_back(matrix[i][left]);
            }
            up++, down--, left++, right--;
        }
        return ans;
    }
};
// @lc code=end


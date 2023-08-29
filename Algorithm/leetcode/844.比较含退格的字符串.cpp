/*
 * @lc app=leetcode.cn id=844 lang=cpp
 *
 * [844] 比较含退格的字符串
 *
 * https://leetcode.cn/problems/backspace-string-compare/description/
 *
 * algorithms
 * Easy (47.89%)
 * Likes:    661
 * Dislikes: 0
 * Total Accepted:    211K
 * Total Submissions: 440.6K
 * Testcase Example:  '"ab#c"\n"ad#c"'
 *
 * 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。
 * 
 * 注意：如果对空文本输入退格字符，文本继续为空。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "ab#c", t = "ad#c"
 * 输出：true
 * 解释：s 和 t 都会变成 "ac"。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "ab##", t = "c#d#"
 * 输出：true
 * 解释：s 和 t 都会变成 ""。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：s = "a#c", t = "b"
 * 输出：false
 * 解释：s 会变成 "c"，但 t 仍然是 "b"。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length, t.length <= 200
 * s 和 t 只含有小写字母以及字符 '#'
 * 
 * 
 * 
 * 
 * 进阶：
 * 
 * 
 * 你可以用 O(n) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
 * 
 * 
 */

// @lc code=start
class Solution
{
public:
    bool backspaceCompare(string s, string t)
    {
        cout << func(s) << endl;
        cout << func(s) << endl;
        return func(s).compare(func(t)) == 0;
    }

    string func(string s)
    {
        int slow = 0, fast = 0;
        int count = 0;
        while (fast < s.length())
        {
            if (s[fast] != '#')
            {
                s[slow] = s[fast];
                slow += 1;
                count += 1;
            }
            else
            {
                if (slow != 0)
                {
                    slow -= 1;
                    count -= 1;
                }
            }
            fast += 1;
        }
        return s.substr(0, count);
    }
};
// @lc code=end


/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 *
 * https://leetcode.cn/problems/minimum-window-substring/description/
 *
 * algorithms
 * Hard (45.31%)
 * Likes:    2637
 * Dislikes: 0
 * Total Accepted:    457.2K
 * Total Submissions: 1M
 * Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
 *
 * 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
 * 。
 * 
 * 
 * 
 * 注意：
 * 
 * 
 * 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
 * 如果 s 中存在这样的子串，我们保证它是唯一的答案。
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "ADOBECODEBANC", t = "ABC"
 * 输出："BANC"
 * 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "a", t = "a"
 * 输出："a"
 * 解释：整个字符串 s 是最小覆盖子串。
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入: s = "a", t = "aa"
 * 输出: ""
 * 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
 * 因此没有符合条件的子字符串，返回空字符串。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * ^m == s.length
 * ^n == t.length
 * 1 <= m, n <= 10^5
 * s 和 t 由英文字母组成
 * 
 * 
 * 
 * 进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
 */

// @lc code=start
class Solution
{
public:
    string minWindow(string s, string t)
    {
        if (s.length() < t.length())
        { // 如果字符串s小于t, 则长度上无法覆盖, 返回空字符串
            return "";
        }
        unordered_map<char, int> map;
        int s_len = s.length(), t_len = t.length();
        // 计算t的相关map
        for (int right = 0; right < t_len; right++)
        {
            map[t[right]]++;
        }
        int count = map.size();
        int left = 0;
        string ans = "";

        for (int right = 0; right < s_len; right++)
        {
            if (t.find(s[right]) != -1)
            {
                auto it = map.find(s[right]);
                --it->second;
                if (it->second == 0)
                {
                    count--;
                }
                if (count == 0)
                {
                    while (count == 0)
                    {
                        if (t.find(s[left]) != -1)
                        {
                            auto it = map.find(s[left]);
                            ++it->second;
                            if (it->second == 1)
                            {
                                count++;
                            }
                        }
                        left++;
                    }
                    string tmp = s.substr(left - 1, right - left + 2);
                    ans = ans.length() > tmp.length() || ans == "" ? tmp : ans;
                }
            }
        }
        return ans;
    }
};
// @lc code=end


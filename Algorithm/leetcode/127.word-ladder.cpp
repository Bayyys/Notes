/*
 * @lc app=leetcode.cn id=127 lang=cpp
 * @lcpr version=30113
 *
 * [127] 单词接龙
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
  int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    // BFS: 从beginWord开始, 依次替换每个位置的字符, 若在wordList中, 则加入队列
    unordered_set<string> word_set(wordList.begin(), wordList.end());
    if (word_set.find(endWord) == word_set.end())
      return 0;                              // endWord不在wordList中
    unordered_map<string, int> visited_map;  // <word, 路径长度>
    queue<string> que;
    que.push(beginWord);
    visited_map.insert(pair<string, int>(beginWord, 1));
    while (!que.empty()) {
      string cur = que.front();
      que.pop();
      int path = visited_map[cur];  // 当前单词的路径长度
      for (int i = 0; i < cur.size(); i++) {
        string new_word = cur;
        // 依次转变单词, 若在wordList中, 则加入队列
        for (int j = 0; j < 26; j++) {
          new_word[i] = 'a' + j;
          if (new_word == endWord) return path + 1;
          if (word_set.find(new_word) != word_set.end() &&
              visited_map.find(new_word) == visited_map.end()) {
            que.push(new_word);
            visited_map.insert(pair<string, int>(new_word, path + 1));
          }
        }
      }
    }
    return 0;
  }
};
// @lc code=end

/*
// @lcpr case=start
// "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
// @lcpr case=end

// @lcpr case=start
// "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
// @lcpr case=end

 */

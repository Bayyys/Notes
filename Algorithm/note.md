[toc]

# 1 数组

## 1.1 数组

1. [704.二分查找](./leetcode/704.二分查找.cpp)
2. [35.搜索插入位置](./leetcode/35.搜索插入位置.cpp)
3. [34.在排序数组中查找元素的第一个和最后一个位置](./leetcode/34.在排序数组中查找元素的第一个和最后一个位置.cpp)
4. [69.x的平方根](./leetcode/69.x的平方根.cpp)
5. [367.有效的完全平方数](./leetcode/367.有效的完全平方数.cpp)

## 1.2 移除元素

1. [27.移除元素](./leetcode/27.移除元素.cpp)
2. [26.删除有序数组中的重复项](./leetcode/26.删除有序数组中的重复项.cpp)
3. [283.移动零](./leetcode/283.移动零.cpp)
4. [844.比较含退格的字符串](./leetcode/844.比较含退格的字符串.cpp)
5. [977.有序数组的平方](./leetcode/977.有序数组的平方.cpp)

## 1.3 有序数组的平方

1. [977.有序数组的平方](./leetcode/977.有序数组的平方.cpp)

## 1.4 长度最小子数组

1. [209.长度最小的子数组](./leetcode/209.长度最小的子数组.cpp)
2. [904.水果成篮](./leetcode/904.水果成篮.cpp)
3. [76.最小覆盖子串](./leetcode/76.最小覆盖子串.cpp)

## 1.5 螺旋矩阵

1. [54.螺旋矩阵](./leetcode/54.螺旋矩阵.cpp)
2. [Offer_29.顺时针打印矩阵](./leetcode/Offer29.顺时针打印矩阵.cpp)

# 2 链表

## 2.1 移除链表元素

1. [203.移除链表元素](./leetcode/203.移除链表元素.cpp)

## 2.2 设计链表

1. [707.设计链表](./leetcode/707.设计链表.cpp)

## 2.3 翻转链表

1. [206.反转链表](./leetcode/206.反转链表.cpp)

## 2.4 交换节点

1. [24.两两交换链表中的节点](./leetcode/24.两两交换链表中的节点.cpp)

## 2.5 删除倒数第N个节点

1. [19.删除链表的倒数第N个节点](./leetcode/19.删除链表的倒数第N个节点.cpp)

## 2.6 链表相交

1. [160.相交链表](./leetcode/160.相交链表.cpp)

## 2.7 环形链表

1. [142.环形链表II](./leetcode/142.环形链表II.cpp)

# 3. 哈希表

## 3.1 理论基础

### 3.1.1 问题解决

>  一般哈希表用来快速判断一个元素是否出现在集合中

### 3.1.2 常见哈希结构

#### 1）数组

#### 2）set(集合)

| 集合                 | 底层实现 | 是否有序 | 数值是否可以重复 | 能否更改数值 | 查询效率 | 增删效率 |
| -------------------- | -------- | -------- | ---------------- | ------------ | -------- | -------- |
| `std::set`           | 红黑树   | 有序     | 否               | 否           | O(log n) | O(log n) |
| `std::multiset`      | 红黑树   | 有序     | 是               | 否           | O(logn)  | O(logn)  |
| `std::unordered_set` | 哈希表   | 无序     | 否               | 否           | O(1)     | O(1)     |


> - 🔑 优先选择 **`std::unordered_set`**
>   - 查询和增删效率是最优的
>
> - 若集合有序，则选用 `std::set`
>
> - 若集合不仅有序还有重复数据，则选用 `std::multiset`

#### 3）map(映射)

| 映射                 | 底层实现 | 是否有序 | 数值是否可以重复 | 能否更改数值 | 查询效率 | 增删效率 |
| -------------------- | -------- | -------- | ---------------- | ------------ | -------- | -------- |
| `std::map`           | 红黑树   | 有序     | 否               | key不可修改  | O(logn)  | O(logn)  |
| `std::multimap`      | 红黑树   | 有序     | 是               | key不可修改  | O(log n) | O(log n) |
| `std::unordered_map` | 哈希表   | 无序     | key不可重复      | key不可修改  | O(1)     | O(1)     |

### 3.1.3 vector方法

> - vector是STL中最常见的容器，它是一种顺序容器，支持随机访问。
> - vector是一块连续分配的内存，从数据安排的角度来讲，和数组极其相似
> - 不同的地方就是
>   - 数组是静态分配空间，一旦分配了空间的大小，就不可再改变了
>     - 扩充机制：按照容器现在容量的一倍进行增长
>     - 扩容后原迭代器失效
>   - 而vector是动态分配空间，随着元素的不断插入，它会按照自身的一套机制不断扩充自身的容量

- 构造

  | -                              | 构造方法                               | 说明 |
  | ------------------------------ | -------------------------------------- |
  | `vector()`                     | 创建一个空vector                       |
  | `vector(int nSize)`            | 创建元素个数为nSize的vector            |
  | `vector(int nSize, const T&t)` | 创建元素个数为nSize，且值为t的vector   |
  | `vector(const vector& v)`      | 复制构造函数                           |
  | `vector(begin, end)`           | 复制[begin, end)区间内另一个数组的元素 |

- 对象操作

  | -                | 调用方法                     | 操作说明 |
  | ---------------- | ---------------------------- |
  | `v.empty()`      | 判断是否为空                 |
  | `v.size()`       | 返回元素个数                 |
  | `v.push_back(t)` | 末尾添加元素                 |
  | `v[n]`           | 返回位置n处的元素            |
  | `v1=v2`          | 以v2替代v1中的元素           |
  | `v1==v2`         | 判断是否相当                 |
  | `!=,<,<=,>,>=`   | 直接用于vector对象的相互比较 |

- 增加函数

| 增加方法                                                                    | 操作说明                                    |
| --------------------------------------------------------------------------- | ------------------------------------------- |
| `void v.push_back(const T& val)`                                            | 末尾添加元素                                |
| `iterator v.insert(iterator it, const T& val)`                              | 向迭代器只想元素前增加一个元素val           |
| `iterator v.insert(iterator it, int n, const T& val)`                       | 向迭代器指向元素前增加n个相同的元素val      |
| `iterator v.insert(iterator it, const_iterator first, const_iterator last)` | 将所给[first, last)迭代器的数据插入到it之前 |

- 删除函数

| 删除方法                                          | 操作说明                   |
| ------------------------------------------------- | -------------------------- |
| `void v.pop_back()`                               | 去掉最后一个数据，返回void |
| `viud v.clear()`                                  | 清空                       |
| `iterator v.erase(iterator it)`                   | 删除迭代器指向元素         |
| `iterator v.erase(iterator first, iterator last)` | 删除[first, last) 中的元素 |

- 遍历函数

| 遍历方法                      | 操作说明                                         |
| ----------------------------- | ------------------------------------------------ |
| `reference v.at(int pos)`     | 返回pos位置元素的引用                            |
| `iterator v.begin()`          | 返回向量头指针，指向第一个元素                   |
| `iterator v.end()`            | 返回向量尾指针，指向向量最后一个元素的下一个位置 |
| `reference v.font`            | 返回首元素的引用                                 |
| `reference v.back()`          | 返回尾元素的引用                                 |
| `reverse_iterator v.rbegin()` | 反向迭代器，指向最后一个元素                     |
| `reverse_iterator v.rend()`   | 反向迭代器，指向第一个元素之前的位置             |

- 其他函数

| 方法                                                       | 操作说明                           |
| ---------------------------------------------------------- | ---------------------------------- |
| `bool v.empty()`                                           | 判断是否为空                       |
| `int v.max_size()`                                         | 返回最大可允许的vector元素数量值   |
| `int v.size()`                                             | 返回元素个数                       |
| `int v.capacity()`                                         | 返回当前vector所能容纳的最大元素值 |
| `void v.swap(vector& v)`                                   | 交换两个同类型向量的数据           |
| `void v.assign(int n, const T& val)`                       | 设置向量中前n个元素的值为val       |
| `void v.assign(const_iterator first, const_iterator last)` | 设置[first, last) 中的元素         |

## 3.2 有效的字母异位词

1. [242.有效的字母异位词](./leetcode/242.valid-anagram.cpp)
2. [383. 赎金信](./leetcode/383.ransom-note.cpp)
3. [49. 字母异位词分组](./leetcode/49.group-anagrams.cpp)
4. [438. 找到字符串中所有字母异位词](./leetcode/438.find-all-anagrams-in-a-string.cpp)

```cpp
// 数组循环遍历的for方法
for (int i = 0; i < n.size(); i++)

for (auto i : n)

for (auto &i : n) // 引用, 可以修改数组中的值

for (auto i = n.begin(); i != n.end(); i++)

for (auto i = n.rbegin(); i != n.rend(); i++) // 反向遍历

for (auto i = n.cbegin(); i != n.cend(); i++) // 常量迭代器, 不可修改数组中的值

for (auto i = n.crbegin(); i != n.crend(); i++) // 常量反向迭代器, 不可修改数组中的值
```

## 3.3 两个数组的交集

1. [349.两个数组的交集](./leetcode/349.intersection-of-two-arrays.cpp)
2. [350. 两个数组的交集 II](./leetcode/350.intersection-of-two-arrays-ii.cpp)

## 3.4 快乐数

1. [202.快乐数](./leetcode/202.happy-number.cpp)

## 3.5 两数之和

1. [1. 两数之和](./leetcode/1.two-sum.cpp)

## 3.6 四数相加II

1. [454.四数相加II](./leetcode/454.4-sum-ii.cpp)

## 3.7 赎金信

1. [383. 赎金信](./leetcode/383.ransom-note.cpp)

## 3.8 三数之和

1. [15.三数之和](./leetcode/15.3-sum.cpp)

## 3.9 四数之和

1. [18.四数之和](./leetcode/18.4-sum.cpp)

# 4. 字符串

## 4.1 反转字符串

1. [344.反转字符串](./leetcode/344.reverse-string.cpp)

## 4.2 反转字符串II

1. [541.反转字符串II](./leetcode/541.reverse-string-ii.cpp)

## 4.3 替换数字

1. [1844.替换所有数字](./leetcode/1844.replace-all-digits-with-characters.cpp)

## 4.4 翻转字符串里的单词

1. [151.翻转字符串里的单词](./leetcode/151.reverse-words-in-a-string.cpp)

## 4.5 实现strStr() KMP算法

1. [28.实现strStr()](./leetcode/28.implement-strstr.cpp)

- 统一减一
```cpp
void getNext(int* next, const string& s) {
    int j = -1;
    next[0] = j;
    for (int i = 1; i < s.size(); i++) {
      while (j >= 0 && s[i] != s[j + 1]) j = next[j];
      if (s[i] == s[j + 1]) j++;
      next[i] = j;
    }
  }
```

- 最长公共前后缀
```cpp
void getNext(int* next, const string& s) {
  int j = 0;
  next[0] = j;
  for (int i = 1; i < s.size(); i++) {
    while (j > 0 && s[i] != s[j]) j = next[j - 1];
    if (s[i] == s[j]) j++;
    next[i] = j;
  }
}
```

## 4.6 重复的子字符串

1. [459.重复的子字符串](./leetcode/459.repeated-substring-pattern.cpp)


# 5. 双指针法

## 5.1 移除元素

1. [27.移除元素](./leetcode/27.remove-element.cpp)
2. [26.删除有序数组中的重复项](./leetcode/26.remove-duplicates-from-sorted-array.cpp)
3. [283.移动零](./leetcode/283.move-zeroes.cpp)
4. [844.比较含退格的字符串](./leetcode/844.backspace-string-compare.cpp)
5. [977.有序数组的平方](./leetcode/977.squares-of-a-sorted-array.cpp)

# 6. 栈与队列

## 6.1 基础理论

### 6.1.1 STL版本

> - STL（C++标准库）

1. HP STL 其他版本的C++ STL，一般是以HP STL为蓝本实现出来的，HP STL是C++ STL的第一个实现版本，而且开放源代码
2. P.J.Plauger STL 由P.J.Plauger参照HP STL实现出来的，被Visual C++编译器所采用，不是开源的
3. **SGI STL** 由Silicon Graphics Computer Systems公司参照HP STL实现，被Linux的C++编译器GCC所采用，SGI STL是开源软件，源码可读性甚高
   - 日常使用此版本

### 6.1.2 构造

- 栈是以底层容器完成其所有的工作，对外提供统一的接口，底层容器是可插拔的（也就是说我们可以控制使用哪种容器来实现栈的功能）

  - 所以STL中栈和队列往往不被归类为容器，而被归类为**container adapter（容器适配器）**

- SGI STL中 队列底层实现缺省情况下一样使用`deque`实现的

  - ```cpp
    // 指定底层实现
    std::stack<int, std::vector<int> > third;  // 使用vector为底层容器的栈
    ```

- SGI STL中队列一样是以`deque`为缺省情况下的底部结构

  - ```cpp
    // 指定底层实现
    std::queue<int, std::list<int>> third; // 定义以list为底层容器的队列
    ```

### 6.1.3 常用操作

- 栈 stack

```cpp
stack<int> s;
s.push(val);	// 将val压入栈顶
s.top();			// 返回栈顶元素
s.pop();			// 弹出栈顶元素
s.size();			// 返回栈中元素的个数
s.empty();		// 检查栈是否为空
```

- 队列 queue

```cpp
queue<int> q;
q.push() 	// 在队尾插入一个元素
q.pop() 	// 删除队列第一个元素
q.size() 	// 返回队列中元素个数
q.empty() // 如果队列空则返回true
q.front() // 返回队列中的第一个元素
q.back() 	// 返回队列中最后一个元素
```

## 6.2 用栈实现队列

1. [232.用栈实现队列](./leetcode/232.implement-queue-using-stacks.cpp)

## 6.3 用队列实现栈

1. [225.用队列实现栈](./leetcode/225.implement-stack-using-queues.cpp)

## 6.4 有效的括号

1. [20.有效的括号](./leetcode/20.valid-parentheses.cpp)

## 6.5 删除字符串中的所有相邻重复项

1. [1047.删除字符串中的所有相邻重复项](./leetcode/1047.remove-all-adjacent-duplicates-in-string.cpp)
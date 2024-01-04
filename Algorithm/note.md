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

1. [203.移除链表元素](./leetcode/203.移除链表元素.cpp)
2. [707.设计链表](./leetcode/707.设计链表.cpp)
3. [206.反转链表](./leetcode/206.反转链表.cpp)
4. [24.两两交换链表中的节点](./leetcode/24.两两交换链表中的节点.cpp)
5. [19.删除链表的倒数第N个节点](./leetcode/19.删除链表的倒数第N个节点.cpp)
6. [160.相交链表](./leetcode/160.相交链表.cpp)

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
3. [202.快乐数](./leetcode/202.happy-number.cpp)
4. [1. 两数之和](./leetcode/1.two-sum.cpp)
5. [454.四数相加II](./leetcode/454.4-sum-ii.cpp)
6. [383. 赎金信](./leetcode/383.ransom-note.cpp)
7. [15.三数之和](./leetcode/15.3-sum.cpp)
8. [18.四数之和](./leetcode/18.4-sum.cpp)

# 4. 字符串

1. [344.反转字符串](./leetcode/344.reverse-string.cpp)
2. [541.反转字符串II](./leetcode/541.reverse-string-ii.cpp)
3. [1844.替换所有数字](./leetcode/1844.replace-all-digits-with-characters.cpp)
4. [151.翻转字符串里的单词](./leetcode/151.reverse-words-in-a-string.cpp)
5. [28.实现strStr()](./leetcode/28.implement-strstr.cpp)

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

## 6.2 题目

1. [232.用栈实现队列](./leetcode/232.implement-queue-using-stacks.cpp)
2. [225.用队列实现栈](./leetcode/225.implement-stack-using-queues.cpp)
3. [20.有效的括号](./leetcode/20.valid-parentheses.cpp)
4. [1047.删除字符串中的所有相邻重复项](./leetcode/1047.remove-all-adjacent-duplicates-in-string.cpp)
5. [150.逆波兰表达式求值](./leetcode/150.evaluate-reverse-polish-notation.cpp)
6. [239. 滑动窗口最大值](./leetcode/239.sliding-window-maximum.cpp)
7. [347.前k个高频元素](./leetcode/347.top-k-frequent-elements.cpp)

## 7. 二叉树

## 7.1 理论基础

```cpp
// 二叉树的定义
struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
}
```

## 7.2 递归遍历

### 7.2.1 遍历方法

- 前序遍历
  ```cpp
  // 中 -> 左 -> 右
  void preorder(TreeNode* cur, vector<int>& vec) {
    if(cur == nullptr) return;
    vec.push_back(cur->val);  // 中
    preorder(cur->left, vec); // 左
    preorder(cur->right, vec);// 右
  }
  ```
- 中序遍历
  ```cpp
  // 左 -> 中 -> 右
  void inorder(TreeNode* cur, vector<int>& vec) {
    if(cur == nullptr) return;
    inorder(cur->left, vec);  // 左
    vec.push_back(cur->val);  // 中
    inorder(cur->right, vec); // 右
  }
  ```
- 后序遍历
  ```cpp
  // 左 -> 右 -> 中
  void postorder(TreeNode* cur, vector<int>& vec) {
    if(cur == nullptr) return;
    postorder(cur->left, vec);  // 左
    postorder(cur->right, vec); // 右
    vec.push_back(cur->val);    // 中
  }
  ```

### 7.2.2 习题

1. [144.二叉树的前序遍历](./leetcode/144.binary-tree-preorder-traversal.cpp)
2. [145. 二叉树的后序遍历](./leetcode/145.binary-tree-postorder-traversal.cpp)
3. [94.二叉树的中序遍历](./leetcode/94.binary-tree-inorder-traversal.cpp)

## 7.3 迭代遍历

### 7.3.1 迭代遍历方法

- 前序遍历
  ```cpp
  // 中 -> 左 -> 右
  vector<int> preorder(TreeNode* root) {
    stack<TreeNode*> st;
    vector<int> res;
    if(root == nullptr) return vec;
    st.push(root);
    while(!st.empty){
      TreeNode* node = st.top();
      st.pop();
      res.push_back(node->val); // 中
      if(node->right) st.push(node->right); // 右(先进后出)
      if(node->left) st.push(node->left); // 左
    }
    return res;
  }
  ```
- 中序遍历
  ```cpp
  // 左 -> 中 -> 右
  vector<int> inorder(TreeNode* root) {
    vector<int> res;
    if(root == nullptr) return vec;
    stack<TreeNode*> st;
    TreeNode* cur=root;
    while(cur!=nullptr || !st.empty()) {
      if(cur!=nullptr) {
        st.push(cur);
        cur = cur->left;
      } else {
        cur = st.top();
        st.pop();
        res.push_back(cur->val); // 中
        cur = cur->right; // 右
      }
    }
    return res;
  }
  ```
- 后序遍历
  ```cpp
  // 左 -> 右 -> 中
  vector<int> postorder(TreeNode* root) {
    stack<TreeNode*> st;
    vector<int> res;
    if(root == nullptr) return vec;
    st.push(root);
    while(!st.empty){
      TreeNode* node = st.top();
      st.pop();
      res.push_back(node->val); // 中
      if(node->left) st.push(node->left); // 左
      if(node->right) st.push(node->right); // 右
    }
    reverse(res.begin(), res.end()); // 反转
    return res;
  }
  ```

### 7.3.2 习题

1. [144.二叉树的前序遍历](./leetcode/144.binary-tree-preorder-traversal.cpp)
2. [145. 二叉树的后序遍历](./leetcode/145.binary-tree-postorder-traversal.cpp)
3. [94.二叉树的中序遍历](./leetcode/94.binary-tree-inorder-traversal.cpp)

## 7.4 统一迭代法

- 前序遍历
  ```cpp
  // 中 -> 左 -> 右
  vector<int> preorder(TreeNode* root) {
    vector<int> res;
    stack<TreeNode*> st;
    if(root!=nullptr) st.push(root);
    while(!st.empty()) {
      TreeNode* node = st.top();
      if (node != nullptr) {
        st.pop();
        if(node->right) st.push(node->right); // 右
        if(node->left) st.push(node->left); // 左
        st.push(node); // 中
        st.push(nullptr); // 空标记
      } else {
        st.pop();
        node = st.top();
        st.pop();
        res.push_back(node->val); // 中
      }
    }
    return res;
  }
  ```
- 中序遍历
  ```cpp
  // 中 -> 左 -> 右
  vector<int> preorder(TreeNode* root) {
    vector<int> res;
    stack<TreeNode*> st;
    if(root!=nullptr) st.push(root);
    while(!st.empty()) {
      TreeNode* node = st.top();
      if (node != nullptr) {
        st.pop();
        if(node->right) st.push(node->right); // 右
        st.push(node); // 中
        st.push(nullptr); // 空标记
        if(node->left) st.push(node->left); // 左
      } else {
        st.pop();
        node = st.top();
        st.pop();
        res.push_back(node->val); // 中
      }
    }
    return res;
  }
  ```
- 后序遍历
  ```cpp
  // 中 -> 左 -> 右
  vector<int> preorder(TreeNode* root) {
    vector<int> res;
    stack<TreeNode*> st;
    if(root!=nullptr) st.push(root);
    while(!st.empty()) {
      TreeNode* node = st.top();
      if (node != nullptr) {
        st.pop();
        st.push(node); // 中
        st.push(nullptr); // 空标记
        if(node->right) st.push(node->right); // 右
        if(node->left) st.push(node->left); // 左
      } else {
        st.pop();
        node = st.top();
        st.pop();
        res.push_back(node->val); // 中
      }
    }
    return res;
  }
  ```

## 7.5 层次遍历

### 7.5.1 层次遍历方法

- 迭代
  ```cpp
  vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> res;
    queue<TreeNode*> q;
    if(root != nullptr) q.push(root);
    while(!q.empty()) {
      int size = q.size();
      vector<int> vec;
      for (int i = 0; i < size; i++) {
        TreeNode* node = q.front();
        q.pop();
        vec.push_back(node->val);
        if(node->left) q.push(node->left);
        if(node->right) q.push(node->right);
      }
      res.push_back(vec);
    }
    return res;
  }
  ```
- 递归
  ```cpp
  void order(TreeNode* root, vector<vector<int>>& res, int depth) {
    if(root == nullptr) return;
    if(res.size() == depth) res.push_back(vector<int>());
    res[depth].push_back(root->val);
    order(root->left, res, depth + 1);
    order(root->right, res, depth + 1);
  }

  vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> res;
    int depth = 0;
    order(root, res, depth);
    return res;
  }
  ```

### 7.5.2 习题

1. [102. 二叉树的层序遍历](./leetcode/102.binary-tree-level-order-traversal.cpp)
2. [107. 二叉树的层序遍历 II](./leetcode/107.binary-tree-level-order-traversal-ii.cpp)
3. [199. 二叉树的右视图](./leetcode/199.binary-tree-right-side-view.cpp)
4. [637. 二叉树的层平均值](./leetcode/637.average-of-levels-in-binary-tree.cpp)
5. [429. N叉树的层序遍历](./leetcode/429.n-ary-tree-level-order-traversal.cpp)
6. [515. 在每个树行中找最大值](./leetcode/515.find-largest-value-in-each-tree-row.cpp)
7. [116. 填充每个节点的下一个右侧节点指针](./leetcode/116.populating-next-right-pointers-in-each-node.cpp)
8. [117. 填充每个节点的下一个右侧节点指针 II](./leetcode/117.populating-next-right-pointers-in-each-node-ii.cpp)
9. [104. 二叉树的最大深度](./leetcode/104.maximum-depth-of-binary-tree.cpp)
10. [111. 二叉树的最小深度](./leetcode/111.minimum-depth-of-binary-tree.cpp)3

## 7.6 其他题目

1. [226.翻转二叉树](./leetcode/226.invert-binary-tree.cpp)
2. [101.对称二叉树](./leetcode/101.symmetric-tree.cpp)
3. [100. 相同的树](./leetcode/100.same-tree.cpp)
4. [572. 另一个树的子树](./leetcode/572.subtree-of-another-tree.cpp)
5. [222.完全二叉树的节点个数](./leetcode/222.count-complete-tree-nodes.cpp)
6. [110.平衡二叉树](./leetcode/110.balanced-binary-tree.cpp)
7. [257.二叉树的所有路径](./leetcode/257.binary-tree-paths.cpp)
8. [404.左叶子之和](./leetcode/404.sum-of-left-leaves.cpp)
9. [513.找树左下角的值](./leetcode/513.find-bottom-left-tree-value.cpp)
10. [112.路径总和](./leetcode/112.path-sum.cpp)
11. [113.路径总和II](./leetcode/113.path-sum-ii.cpp)
12. [106.从中序与后序遍历序列构造二叉树](./leetcode/106.construct-binary-tree-from-inorder-and-postorder-traversal.cpp)
13. [105.从前序与中序遍历序列构造二叉树](./leetcode/105.construct-binary-tree-from-preorder-and-inorder-traversal.cpp)
14. [654.最大二叉树](./leetcode/654.maximum-binary-tree.cpp)
15. [617.合并二叉树](./leetcode/617.merge-two-binary-trees.cpp)
16. [700.二叉搜索树中的搜索](./leetcode/700.search-in-a-binary-search-tree.cpp)
17. [98.验证二叉搜索树](./leetcode/98.validate-binary-search-tree.cpp)
18. [530.二叉搜索树的最小绝对差](./leetcode/530.minimum-absolute-difference-in-bst.cpp)
19. [501.二叉搜索树中的众数](./leetcode/501.find-mode-in-binary-search-tree.cpp)
20. [236.二叉树的最近公共节点](./leetcode/236.lowest-common-ancestor-of-a-binary-tree.cpp)
21. [235.二叉搜索树的最近公共节点](./leetcode/235.lowest-common-ancestor-of-a-binary-search-tree.cpp)
22. [701.二叉搜索树中的插入操作](./leetcode/701.insert-into-a-binary-search-tree.cpp)
23. [450.删除二叉搜索树中的节点](./leetcode/450.delete-node-in-a-bst.cpp)
24. [669.修剪二叉搜索树](./leetcode/669.trim-a-binary-search-tree.cpp)
25. [108.将有序数组转换为二叉搜索树](./leetcode/108.convert-sorted-array-to-binary-search-tree.cpp)
26. [538.把二叉搜索树转换为累加树](./leetcode/538.convert-bst-to-greater-tree.cpp)

# 8. 回溯算法

> - 回溯法也可以叫做回溯搜索法，它是一种搜索的方式
> - 效率: 回溯的本质是穷举, 穷举所有可能, 然后选出我们想要的答案, 所以回溯算法的时间复杂度一般都很高

```c
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
```

## 8.1 题目

1. [77.组合](./leetcode/77.combinations.cpp)
2. [216.组合总和III](./leetcode/216.combination-sum-iii.cpp)
3. [17.电话号码的字母组合](./leetcode/17.letter-combinations-of-a-phone-number.cpp)
4. [39.组合总和](./leetcode/39.combination-sum.cpp)
5. [40.组合总和II](./leetcode/40.combination-sum-ii.cpp)
6. [131.分割回文串](./leetcode/131.palindrome-partitioning.cpp)
7. [93.复原IP地址](./leetcode/93.restore-ip-addresses.cpp)
8. [78.子集](./leetcode/78.subsets.cpp)
9. [90.子集II](./leetcode/90.subsets-ii.cpp)
10. [491.递增子序列](./leetcode/491.increasing-subsequences.cpp)
11. [46.全排列](./leetcode/46.permutations.cpp)
12. [47.全排列II](./leetcode/47.permutations-ii.cpp)
13. [332.重新安排行程](./leetcode/332.reconstruct-itinerary.cpp)
14. [51.N皇后](./leetcode/51.n-queens.cpp)
15. [37.数独](./leetcode/37.sudoku-solver.cpp)

# 9. 贪心算法

## 9.1 相关题目

1. [455.分发饼干](./leetcode/455.assign-cookies.cpp)
2. [376.摆动序列](./leetcode/376.wiggle-subsequence.cpp)
3. [53.最大子数组和](./leetcode/53.maximum-subarray.cpp)
4. [122.买卖股票的最佳时机II](./leetcode/122.best-time-to-buy-and-sell-stock-ii.cpp)
5. [55.跳跃游戏](./leetcode/55.jump-game.cpp)
6. [45.跳跃游戏II](./leetcode/45.jump-game-ii.cpp)
7. [1005.k次取反后最大化的数组和](./leetcode/1005.maximize-sum-of-array-after-k-negations.cpp)
8. [134.加油站](./leetcode/134.gas-station.cpp)
9. [135.分发糖果](./leetcode/135.candy.cpp)
10. [860.柠檬水找零](./leetcode/860.lemonade-change.cpp)
11. [406.根据身高重建队列](./leetcode/406.queue-reconstruction-by-height.cpp)
12. [452.用最少数量的箭引爆气球](./leetcode/452.minimum-number-of-arrows-to-burst-balloons.cpp)
13. [435.无重叠区间](./leetcode/435.non-overlapping-intervals.cpp)
14. [763.划分字母区间](./leetcode/763.partition-labels.cpp)
15. [56.合并区间](./leetcode/56.merge-intervals.cpp)
16. [738.单调递增的数字](./leetcode/738.monotone-increasing-digits.cpp)
17. [968.监控二叉树](./leetcode/968.binary-tree-cameras.cpp)

# 10. 动态规划

## 10.1 理论基础

- 动态规划 (Dynamic Programming, DP): 通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法
  - 动态规划常常适用于有重叠子问题和最优子结构性质的问题
- 解题步骤
  1. 确定 **DP数组** 以及下标的定义
  2. 确定递推公式
  3. DP数组如何初始化
  4. 确定遍历顺序
  5. 举例推导DP数组
- debug方式: **打印dp数组**

## 10.2 相关题目

1. [509.斐波那契数](./leetcode/509.fibonacci-number.cpp)
2. [70.爬楼梯](./leetcode/70.climbing-stairs.cpp)
3. [746.使用最小花费爬楼梯](./leetcode/746.min-cost-climbing-stairs.cpp)
4. [62.不同路径](./leetcode/62.unique-paths.cpp)
5. [63.不同路径II](./leetcode/63.unique-paths-ii.cpp)
6. [343.整数拆分](./leetcode/343.integer-break.cpp)
7. [96.不同的二叉搜索树](./leetcode/96.unique-binary-search-trees.cpp)
8. [416.分割等和子集](./leetcode/416.partition-equal-subset-sum.cpp)
9. [1049.最后一块石头的重量II](./leetcode/1049.last-stone-weight-ii.cpp)
10. [494.目标和](./leetcode/494.target-sum.cpp)
11. [474.一和零](./leetcode/474.ones-and-zeroes.cpp)
12. [518.零钱兑换II](./leetcode/518.coin-change-2.cpp)
13. [377.组合总和IV](./leetcode/377.combination-sum-iv.cpp)
14. [70.爬楼梯](./leetcode/70.climbing-stairs.cpp)
15. [322.零钱兑换](./leetcode/322.coin-change.cpp)
16. [279.完全平方数](./leetcode/279.perfect-squares.cpp)
17. [139.单词拆分](./leetcode/139.word-break.cpp)
18. [198.打家劫舍](./leetcode/198.house-robber.cpp)
19. [213.打家劫舍II](./leetcode/213.house-robber-ii.cpp)
20. [337.打家劫舍III](./leetcode/337.house-robber-iii.cpp)
21. [121.买卖股票的最佳时机](./leetcode/121.best-time-to-buy-and-sell-stock.cpp)
22. [122.买卖股票的最佳时机II](./leetcode/122.best-time-to-buy-and-sell-stock-ii.cpp)
23. [123.买卖股票的最佳时机III](./leetcode/123.best-time-to-buy-and-sell-stock-iii.cpp)
24. [188.买卖股票的最佳时机IV](./leetcode/188.best-time-to-buy-and-sell-stock-iv.cpp)
25. [309.最佳买卖股票时机含冷冻期](./leetcode/309.best-time-to-buy-and-sell-stock-with-cooldown.cpp)
26. [714.买卖股票的最佳时机含手续费](./leetcode/714.best-time-to-buy-and-sell-stock-with-transaction-fee.cpp)
27. [300.最长递增子序列](./leetcode/300.longest-increasing-subsequence.cpp)
28. [674.最长连续递增序列](./leetcode/674.longest-continuous-increasing-subsequence.cpp)
29. [718.最长重复子数组](./leetcode/718.maximum-length-of-repeated-subarray.cpp)

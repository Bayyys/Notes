# 第 8 章 函数探幽

> C++区别于C语言，提供了新特性：包括 **内联函数**、**按引用传递变量**、**默认的参数值**、**函数重载**（**多态**）以及**模板函数**。

# 1. 内联函数 inline

> 编译过程的目标是可执行程序（由一组机器语言指令组成）。运行程序时，操作系统将指令载入到计算机内存中，则每条指令都有其特定的内存地址。
>
> 内联函数的编译代码与其它程序代码内联，编译器就使用相应的函数代码替换函数调用。
>
> - 为提高程序运行速度作出的改进

## 1.1 常规函数和内联函数

- **常规函数**：调用使得程序调到另一个地址（函数的地址），并在函数结束时返回。

> 将程序流程转到独立的函数

- **内联函数**：程序无需跳到另一个位置处执行代码，再跳回来。

> 用内联函数的代码来替换函数调用

## 1.2 内联函数的优缺点

**优点**：运行速度比常规函数快。

**缺点**：占用内存大

## 1.3 使用内联函数的要求

- 声明和定义前都需要加关键字 `inline`
  - :key: 省略原型，将整个定义（函数头和所有函数代码）放在本应提供原型的地方。

- :warning: 内联函数不能递归

```C++
#include<iostream>

inline double square(double x){return x*x;}

int main()
{
	using namespace std;
	double a,b;
	double c = 13.0;
	a = square(5.0);
	b = square(4.5 + 7.5);
	cout << "a = "<<a<<" , b = "<<b<<"\n"; // a =25 b = 144
	cout << "c = "<<c; //c = 13
	cout << ", c squared = "<<square(c++)<<"\n"; // c = 14*14=169
	cout << "Now c = "<<c<<"\n"; //c=14
	return 0;
}
```

## 1.4 内联和宏

>  inline是C++新增特性

> :key: **内联函数**和**宏**
>
> 在C语言中使用`预处理器#define`来提供宏。————> 内联代码的原始实现。
>
> ```c
> #define SQUARE(x) x*x
> ```
>
> 此时不是通过传递参数实现，而是通过文本替换来实现。

- **宏的缺点**：不能按值传递
- 使用C语言的宏执行了类似函数的功能，应考虑将它们转换为C++内联函数

# 2. 引用变量

> C++新增的复合类型

- **引用**：已定义变量的别名。

- **主要用途**：用作 函数形参。通过引用变量用作参数，函数将使用原始数据，而不是使用副本。

## 2.1 创建引用变量

> `&` 作为**引用**的类型标识符

```c++
int rats;
int & rodents = rats;
```

- 引用必须在**声明引用时将其初始化**

> 指针的使用可以 先声明，再赋值

## 2.2 引用用作函数参数

- **引用传递**：当引用被用作`函数参数`时，使得函数中的变量名成为`调用程序中的变量的别名`。

> 允许被调用的函数能够`访问调用函数`中的变量。

- **按值传递**：被调用函数使用调用程序的值的**拷贝**。


> C语言中改用按指针传递的方式避开按值传递的限制。

使用和访问原始数据的方法：按 **`引用传递`** 和 **`传递指针`**。

当左值引用参数是 const时，会生成临时变量的两种情况：
> 左值参数：可被引用的数据对象。

- 实参的类型正确，但不是左值。

- 实参的类型不正确，但可转换为正确的类型。

**尽可能使用const**

>- 使用const可以避免无意中修改数据的编程错误
>
>- 使用const使函数能够处理`const`和`非const实参` ，否则只能接受`非const数据`。
>
>- 使用`const引用`使函数能够正确生成并使用`临时变量`(如果`实参`和`引用参数`不匹配，c++将生成`临时变量`)。

C++11 引入 **`右值引用`**，可指向右值，使用 `&&` 来声明。

代码例子 👇
```cpp
#include<iostream>

using namespace std;

double cube(double a);
double refcube(const double &ra); // 使用const的目的：防止引用的参数被修改。

int main()
{
    double x = 3.0;
    cout<<x<<" 的立方为: "<<cube(x)<<endl;
    cout<<x<<" 的立方为："<<refcube(x)<<endl;
    return 0;
}
double cube(double a)
{
    return a*a*a;
}
double refcube(const double &ra)
{
    return ra*ra*ra;
}
```

⚠️注意：如果函数调用的参数不是左值或与相对应的const引用参数的类型不匹配，则C++将创建类型正确的匿名变量，将函数调用的参数的值传递给匿名变量，并让参数来引用该变量。


## 2.3 结构引用

引用适合 **结构和类**（用户自定义类型，非基本的内置类型）。

**<u>引入引用的目的</u>**：用于用户自定义类型，而不是基本的内置类型。

使用 `结构引用参数`的方式 与`基本变量引用` 相同，只需在声明结构参数时使用 `引用运算符&` 即可。

代码例子 👇
```cpp
#include<iostream>
#include<string>

using namespace std;

/*创建结构*/
struct free_throws
{
    string name;
    int made;
    int attempts;
    float percent;
};

/*声明函数原型*/
void display(const free_throws & ft); 
void set_pc(free_throws & ft);
free_throws & accumulate(free_throws & target,const free_throws & source);

int main()
{
    /*对部分初始化，其余部分设置为0*/
    free_throws one = {"ifelsa branch",13,14};
    free_throws two = {"Andor Knott",10,16};
    free_throws three = {"Minnie Max",7,9};
    free_throws four = {"Whily Looper",5,9};
    free_throws five = {"Long Long",6,14};
    free_throws team = {"Throwgoods",0,0};

    /*不做初始化*/
    free_throws dup;

    set_pc(one); /*set_pc中的ft为引用，按值传递不可行*/
    display(one); /*使用const引用参数，可以使用按值传递结构，但是使用引用的好处：可以节省时间和内存*/
    accumulate(team,one); /*第一个参数：引用 ———— 可修改，第二个参数：const引用*/
    display(team);

    /*使用返回值作为参数*/
    display(accumulate(team,two));
    accumulate(accumulate(team,three),four);
    display(team);

    /*使用返回值进行赋值*/
    dup = accumulate(team,five); /*添加five的数据给dup*/
    cout<<"Displaying team:\n";
    display(team);
    cout<<"Displaying dup after assignment:\n";
    display(dup);
    set_pc(four);

    /*ill-advised assignment*/
    
    /*将five的数据添加到dup中，再使用four的内容覆盖dup的内容。返回类型是const，不可修改，所以赋值不合法。*/
    accumulate(dup,five) = four;   
    cout<<"Displaying dup after ill-advised assignment:\n";
    display(dup);
    return 0;
}

/*输出展示*/
void display(const free_throws & ft)
{
    cout<<"Name : "<<ft.name<<'\n';
    cout<<"Made : "<<ft.made<<'\t';
    cout<<"Attempts : "<<ft.attempts<<'\t';
    cout<<"Percent : "<<ft.percent<<'\n';
}

/*计算*/
void set_pc(free_throws & ft)
{
    if(ft.attempts!=0)
        ft.percent = 100.0f * float(ft.made)/float(ft.attempts);
    else
        ft.percent = 0;    
}

/**/
free_throws & accumulate(free_throws & target,const free_throws & source) /*const类型，所以不可修改*/ 
{
    target.attempts += source.attempts;
    target.made += source.made;
    set_pc(target);
    return target;
}
```

## 2.4 返回引用时的注意事项

避免返回函数终止时不再存在的内存单元引用。原因：函数运行完毕后将不存在。

~~杜绝使用临时变量的引用~~

```cpp
const free_throws & clone2(free_throws &ft)
{
	free_throws newguy; 
	newguy = ft; // 拷贝
	return newguy; //返回拷贝引用，返回一个指向临时变量newguy的引用，函数执行完毕后则不存在。
}
```
> 解决方法：
> 
> 1.返回一个作为参数传递给函数的引用。作为参数的引用将指向调用函数使用的数据，返回的引用也随之指向所使用的数据。
>
> 2.使用`new`来分配新的存储空间，使得返回指向该内存空间的指针。👉**小缺点**：会忘记使用 `delete` 来`释放内存`。

改进后：
```C++
const free_throws & clone(free_throws &ft)
{
	free_throws *pt; //使用指针指向结构，所以*pt可直接代表 free_throws这个结构
	*pt = ft; //拷贝信息
	return *pt; //返回
}
```

如果返回一个结构，而不是指向结构的引用，将整个结构复制到一个临时变量，再将临时变量拷贝。效率比其他传递方式高。

## 2.5 对象、继承和引用

**继承**：将语言的特性从`一个类` *传递* 给`另一个类`。

**继承的特征**：派生来继承了基类的方法，基类引用可以指向派生类对象，而`无需进行强制类型转换`。
> `ostream`是基类
>
> `ofstream`是派生类

## 2.7 何时使用引用参数

***使用引用参数的两个主要原因***
- 程序员能修改调用函数中的数据对象。
- 通过传递引用而不是整个数据对象，提高程序的运行速度。（当数据对象（结构和类对象）较大时很重要）

***对于 `使用传递的值` 而 `不作修改` 的函数***
- 数据对象`很小`，如`内置数据类型或小型结构`，**`按值传递`**；
- 数据对象是`数组`，则使用`指针`，因为这是唯一的选择，并将 **`指针声明为指向 const 的指针`**；
- 数据对象是`较大的结构`，则使用 `const 指针`或 `const 引用`，可以 ***节省复制结构所需的时间和空间***；
- 数据对象是`类对象`，则使用 `const 引用`。传递类对象参数的标准方式是 **`按引用传递`**。

***对于`修改调用函数中数据`的函数***

- 数据对象是`内置数据类型`，则使用`指针`；

- 数据对象是`数组`，则`只能`使用`指针`；

- 数据对象是`结构`，则使用`引用或指针`；

- 数据对象是`类对象`，则使用`引用`。


# 3. 默认参数
**定义**：指当函数调用中省略了实参时自动使用的一个值。

设置默认值的方法：通过函数原型将值赋给原型中的参数。例left() 原型：
```cpp
char *left(const char *str,int n = 1);
```

对于`带参数列表`的函数，必须`从右向左`添加默认值（要为某个参数设置默认值，必须为其右边的所有参数提供默认值）。
```cpp
int harpo(int n,int m = 4 , int j = 5); //VALID
int chico(int n ,int m = 6,int j); // INVALID
```

实参按 `从左向右` 的顺序依次被赋给相应的形参，而~~不能跳过任何参数~~。
```cpp
beeps = harpo(3, ,8); // 不允许
```

**👉 默认参数的好处**：*减少要定义的析构函数、方法以及方法重载的数量**。

⚠️注意：只有原型指定了默认值，函数定义与没有默认参数时完全相同。

```cpp
#include<iostream>
const int ArSize = 80;
char *left(const char * str,int n = 1);
int main()
{
    using namespace std;
    char sample[ArSize];
    cout <<"Enter a string : \n";
    cin.get(sample,ArSize);
    char * ps = left(sample,4);
    cout << ps << endl;
    delete [] ps;
    ps = left(sample);
    cout << ps << endl;
    delete [] ps;
    return 0;
}
char *left(const char *str,int n)
{
    if(n<0)
        n = 0;
    char *p = new char[n+1];
    int i;
    for(i = 0;i < n && str[i];i++)
        p[i] = str[i];
    while(i<=n)
        p[i++] = '\0';
    return p;
}
```
设置新字符串程度的方法：使用 `strlen()` 函数。
```cpp
int len = strlen(str);
n = (n < len)?n:len
char *p = new char[n+1];
```
- C程序倾向于运行速度快，代码简洁。
- C++追求可靠性。

# 4. 函数重载（polymorphism）

- `默认参数`可以使用不同数目的参数调用同一个函数。
- 术语`多态（polymorphism）` 指多种形式，函数多态允许函数使用多种形式。
- 术语`函数重载` 指可以有多个同名的函数，则对名称进行重载。
> `函数多态（函数重载）`可使用多个同名的函数。

函数重载的关键是`函数的参数列表` ---> 函数`特征标`。

C++允许定义`名称相同`的函数，条件是`特征标不同`。

编译器在检查函数特征标时，将把类型引用和类型本身视为同一个特征标。
> 匹配函数时，不区分`const` 和`非const变量`。

⚠️注意：真正让函数能够进行重载的是：**特征标**。

## 4.1 左值引用和右值引用（自我扩展补充）
C++ 11 中新增特性 👇 

更多关于右值引用细节请关注 [Chapter18 内容](../Chapter18/README.md)
或者如下链接文章

超级简单易懂的讲解文章参考  👉 「[腾讯技术过程 一文读懂C++右值引用和std::move](https://zhuanlan.zhihu.com/p/335994370)」完整位置请移步，以下内容个人笔记原因，随意进行了缩减，请大佬团队高抬贵手不要发律师函告知抄袭。

区分`左值`和`右值`的方法：查看能否对其进行`取地址`操作。
> 可取地址，位于等号左边 ---> 左值
>
> 不可取地址，位于等号右边 ---> 右值

✅ 参考文章总结：有地址的变量就是左值，没有地址的字面值、临时值就是右值。

- **左值引用**
能指向左值，不能指向右值的就是左值引用。
```cpp
int a = 5;
int &ref_a = a; // 左值引用指向左值，编译通过
int &ref_a = 5; // 左值引用指向了右值，会编译失败
```
**引用是变量的别名，由于右值没有地址，没法被修改，所以左值引用无法指向右值。** 但const左值引用是可以指向右值
```cpp
const int &ref_a = 5;
```
> 原因：const左值引用不会修改指向值，因此可以指向右值。

- **右值引用**

**右值引用的标志是`&&`**。

右值引用专门为右值而生，**可以指向右值，不能指向左值**
```cpp
int &&ref_a_right = 5; // ok
 
int a = 5;
int &&ref_a_left = a; // 编译不过，右值引用不可以指向左值
 
ref_a_right = 6; // 右值引用的用途：可以修改右值
```

**被声明出来的左、右值引用都是左值。 因为被声明出的左右值引用是有地址的，也位于等号左边。**

## 4.2 何时使用函数重载？
函数重载不可滥用。仅当函数基本上执行相同的任务，但使用不同形式的数据时，才应采用函数重载。


# 5. 函数模版
## 5.1 重载的模板
- 函数模板是**通用**的**函数描述**，使用**泛型**（可用具体的类型替换）来定义函数。所以也叫做**通用编程**。


- 建立一个模板，关键字 `template` 和 `typename` 是必需，除非使用`关键字class`代替typename，必须使用 `尖括号<>`。

```cpp
template <typename T> 	/*C++98 标准时添加关键字 typename*/
template <class Anytype> 		/*C++98之前使用class*/
```

> :key: 如果需要多个将`同一种算法`用于`不同类型的函数`，请使用`模板`。如果不考虑向后兼容的问题，并愿意键入较长的单词，则`声明类型参数`时，应使用关键字`typename`而不是`class`。
>
> :warning: 注意：函数模板不能缩短可执行程序。
>
> :key: 模板重载和函数重载类似
>
> :key: 常见的使用情形是，在头文件中声明模板，并在需要使用模板的文件中包含头文件

## 5.2 模板的局限性

- 编写的模板函数很可能无法处理某些类型

```cpp
template <class T> /*等于 template <typename T>*/
void f(T a,T b)
{
    a=b; 		/*如果T为数组时，假设不成立*/
    if(a > b) 	/*如果T为结构时，假设不成立*/
}
```

- 解决方案
  1. 重载运算符，以便能够将其用于特定的结构或类
  2. 为特定类型提供具体化的模板定义

## 5.3 显式具体化

> 第三代具体化（ISO/ANSI C++标准）

- 当编译器找到与函数调用匹配的具体化定义时，将使用该定义，而不再寻找模板。


C++98标准使用的方法
- 对于给定的函数名，可以有**非模板函数**、**模板函数**和**显式具体化模板函数**以及他们的**重载版本**。
- 显示具体化的原型和定义应以`template<>`打头，并**通过名称来指出类型**。
- 具体化优先于常规模板，而非模板函数优先于具体化和常规模板。

显式具体化的格式：
```cpp
template <> void Swap<int>(int&,int&)
```

## 5.4 实例化和具体化

**隐式实例化**：编译器在使用模板事会为特定类型生成函数定义时，即可实现模板实例。

**显式实例化**：直接告知编译器创建特定的实例。
```cpp
/* 语法：声明所需的类 ----> 用符号 <> 符号指示类型，并在声明前加上关键字template */
template void Swap<int>(int,int);	// 显式实例化
```
> :warning: 注意：显式具体化声明在关键字template后包含<>，而显式实例化没有。
>
> :x: 警告：不要试图在同一个文件（或转换单元）中使用同一种类型的显式实例和显式具体化，否则会出错。

## 5.5 编译器选择使用哪个函数版本

### 5.5.1 重载解析

**重载解析**：决定为函数调用使用哪一个函数定义的过程。

- 解析的过程
  1. 创建**候选函数列表**，包含被调用函数名称相同的所有函数
  2. 使用候选函数列表创建**可执行函数列表**，这些都是参数数目正确的函数，为此有一个隐式转换序列，其中包括实参类型和相应的形参类型完全匹配的情况
  3. 确定是否有**最佳可执行函数**，如果有则调用，没有则报错


### 5.5.2 完全匹配和最佳匹配

| 实参                | 形参                    |
| ------------------- | ----------------------- |
| Type                | Type&                   |
| Type&               | Type                    |
| Type[]              | *Type                   |
| Type(argument-list) | Type(*) (argument-list) |
| Type                | const Type              |
| Type                | volatile Type           |
| Type *              | const Type              |
| Type *              | volatile Type*          |

### 5.5.3 创建自定义选择

```cpp
fun(x, y);			// 与模板进行匹配
fun<>(x, y);		// 选择模板函数，而不是非模板函数
fun<int>(x, y);		// 进行显式实例化
```

## 5.6 函数模板的发展

### 5.6.1 关键词 decltype

> :round_pushpin: C++11

```cpp
template<typename T1, typename, T2>
void ft(T1 x, T2 y) {
    ...
    decltype(x+y) xpy = x + y;
    ...
}
```

- 对于不确定的数据类型，可以以此表示

  - 以上代码表示，相加得到的类型可能与 (x+y) 同类型

- `decltype(expression) var;`

- 确定类型的核对表

  > :key: **并不会实际调用函数。编译器通过查看函数的原型来获悉返回类型，而无需实际调用函数**

  1. 如果 `expression `是一个没有用括号括起的标识符，则 `var` 的类型与该标识符的类型相同，包括 `const` 等限定符；

  2. 如果 `expression `是一个函数调用，则 `var `的类型与函数的返回类型相同；

  3. 如果`expression`是一个左值，则`var `为指向其类型的引用；

     - ```cpp
       double xx = 4.4;
       decltype((xx)) r2 = xx;	// r2 is double &
       decltype(xx) w = xx;	// w is double
       ```

       > 一种主要的情况为，括号括起的标识符

  4. 如果前面的条件都不满足，则 `var`的类型与`expression` 的类型相同；

- 若要多次声明，可以结合 `typedef` 和 `decltype`

  - `typedef decltype(x+y) xytype;`

### 5.6.2 后置返回类型

> :round_pushpin: C++11

:question: **返回值类型无法确认** -> **auto**

```cpp
template<typename T1, typename T2>
auto gt(T1 x, T2 y) -> decltype(x+y) {
    ...
    return x+y;
}
```


## *

> HTML + CSS + JavaScript
>
> 结构 + 表现 + 动作
>
> - ==结构==化标准语言（HTML，XML)
> - ==表现==标准语言(CSS)
> - ==行为==标准语言（DOM,ECMAScript)

## 特殊HTML字符

| HTML源码 | 显示结果 | 描述                   |
| -------- | -------- | ---------------------- |
| \&lt;    | <        | 小于号显示标记         |
| \&gt;    | >        | 大于号或显示标记       |
| \&amp;   | &        | 可用于显示其他特殊字符 |
| \&quot;  | ''       | 引号                   |
| \&reg;   | ©        | 已注册                 |
| \&copy;  | ®        | 版权                   |
| \&trade; | TM       | 商标                   |
| \&ensp;  |          | 半个空白位             |
| \&emsp;  |          | 一个空白位             |
| \&nbsp;  |          | 不断行的空白           |



## CSS简介

### CSS

- Cascading Style Sheet - 层叠样式表
- CSS - 表现(美化网页)
- 字体，颜色，边距，高度，宽度，背景图片，网页定位，网页浮动

![HTML-CSS](https://s2.loli.net/2023/05/13/4XHPT18dIgVf9Uo.png)

### 发展史

- CSS1.0

- CSS2.0：DIV（块）+CSS，HTML与CSS结构分离的思想，网页变得简单，SEO(搜索引擎优化)

  - > SEO： Search Engine Optimization, 搜索引擎优化。利用搜索引擎的规则提高网站在有关搜索引擎内的自然排名。目的是让其在行业内占据领先地位，获得品牌收益。很大程度上是网站经营者的一种商业行为，将自己或自己公司的排名前移。SEO是提高你网站排名的一个很有效的方法，这个完善和优化你网站的排名因素的方法就是能影响搜索引擎的排名的算法。 因此，SEO是网络营销策略 （online marketing Digital strategy）和数字营销策略 （Digital Marketing strategy）中很重要的一个环节。SEO使你的网站获取得更多的流量（traffic）同时也可以提高你在搜索引擎的排名。那就意味你可以获取得更多的订单，更多的利润。

- CSS2.1：浮动，定位

- CSS3.0：圆角、阴影、动画…浏览器兼容性~

### 快速入门

```css
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!--  规范
    语法:
        选择器 {
            声明1; => 属性: 值;
            声明2;
            ...
        }
    -->

    <style>
        h1{
            color: red;

        }
    </style>
</head>
```

- 推荐html与css分离写法

![image-20230513194036558](C:/Users/bayyy/AppData/Roaming/Typora/typora-user-images/image-20230513194036558.png)

```css
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="css/style.css">
</head>

<!-- style.css -->
h1{
    color: red;
}
```

css注释：`/* css注释 */`

### CSS优势

1. 内容和表现分离；
2. 网页结构表现统一，可以实现复用
3. 样式十分的丰富
4. 建议使用独立于html的css文件
5. 利用SEO，容易被搜索引擎收录！

### CSS的3种导入方式

#### 三种样式

- 内部样式
- 外部样式==推荐==
- 行内样式

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!--    内部样式    -->
    <style>
        /* css 注释 */
        h1 {
            color: red;

        }
    </style>

    <!--   外部样式    -->
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<h1>我是标题</h1>

<!-- 应用优先级: 行内样式 > 内部样式 > 外部样式 -->
<!-- 行内样式: 在标签元素中，编写一个style属性，编写样式即可 -->
<h1 style="color: blue">我也是标题</h1>
</body>
</html>
```

#### 外部样式两种导入方式

- 链接方式

  - ```html
    <!--外部样式-->
        <link rel="stylesheet" href="css/style.css" />
    ```

- 导入方式

  - @import是CSS2.1特有的！

  - ```html
    <!--导入式-->
        <style>
            @import url("css/style.css");
        </style>
    
    ```

## 选择器

> 作用：选择页面上的某一个后者某一类元素

### 基本选择器

- 优先级：id选择器 > class选择器 > 标签选择器

#### 标签选择器

```html
<head>
    <meta charset="UTF-8">
    <title>标签选择器</title>

    <!-- 标签选择器: 选择所有的标签 -->
    <style>
        h1 {
            color: #ff0000;
            background: bisque;
            border-radius: 24px;
        }
        p{
            font-size: 80px;
            border-bottom: aqua 2px solid;
        }
    </style>
</head>
<body>
<h1>Bayyys</h1>
<h1>bayyys</h1>
<p>bay</p>
</body>
```

#### 类选择器

```html
<head>
    <meta charset="UTF-8">
    <title>类选择器</title>

    <style>
        /* 类选择器: .class名称{} */
        /* 选择所有的class属性值为class1的标签 */
        /* 可以多个标签归类，可以复用 */
        .class1 {
            color: #ff0000;
            background: bisque;
            border-radius: 24px;
        }
        .class2 {
            font-size: 80px;
            border-bottom: aqua 2px solid;
        }
    </style>

</head>
<body>
<h1 class="class1">标题1</h1>
<h1 class="class2">标题2</h1>
<h1>标题3</h1>
</body>
```

#### id选择器

```html
<head>
    <meta charset="UTF-8">
    <title>id选择器</title>

  <style>
    /* id选择器: #id名称{} */
    /* id选择器 > 类选择器 > 标签选择器 */
    #id1 {
      color: #ff0000;
      background: bisque;
      border-radius: 24px;
    }
    #id2 {
      font-size: 80px;
      border-bottom: aqua 2px solid;
    }
    .class1 {
      color: #ff0000;
      background: bisque;
      border-radius: 24px;
    }
  </style>
</head>
<body>
<h1 id="id1">标题1</h1>
<h1 id="id2" class="class1">标题2</h1>
<h1 class="class1">标题3</h1>
</body>
```

### 层次选择器

#### 后代选择器

```html
/* 后代选择器: 元素后面的所有代 */
body p {
    color: green;
    background: red;
}
```

#### 子选择器

```html
/* 子代选择器: 只有一代 */
body>p {
    color: blue;
    background: yellow;
}
```

#### 相邻兄弟选择器

```html
/* 相邻兄弟选择器: 选择紧跟在另一个元素后的元素,且二者有相同的父元素(紧跟着的下一个) */
.active+p {
    color: yellow;
    background: blue;
}
```

#### 通用选择器

```html
/* 通用选择器: 元素后的所有同级元素,且二者有相同的父元素(所有的后级元素) */
.usual~p {
    color: red;
    background: blue;
}
```

### 结构伪类选择器

```html
<!-- 伪类选择器: 选择元素的特殊状态 -->
<!-- 避免使用 class id 选择器 -->
<style>
    ul li:first-child {
        color: green;
        background: red;
    }
    ul li:last-child {
        color: blue;
        background: yellow;
    }
    /* 选中当前元素的父级元素, 选中父级元素的第n个, 并且是当前类型元素才可生效(按照顺序选择) */
    p:nth-child(2) {
        color: red;
        background: green;
    }
    /* 选中当前元素的父级元素, 选中父级元素的第n个此类型的元素(按照类型选择) */
    p:nth-of-type(2) {
        color: green;
        background: red;
    }
</style>

<body>
    <h1>h1</h1>
    <p>p1</p>
    <p>p2</p>
    <p>p3</p>
    <ul>
        <li>li1</li>
        <li>li2</li>
        <li>li3</li>
    </ul>
</body>
```

![image-20230513204516044](https://s2.loli.net/2023/05/13/bndJecG2apuVtTi.png)

### 属性选择器

```html
<head>
    <meta charset="UTF-8">
    <title>属性选择器</title>
    <style>
        .demo a {
            float: left;
            display: block;
            height: 50px;
            width: 50px;
            border-radius: 10px;
            background: blue;
            text-align: center;
            color: gray;
            text-decoration: none;
            margin: 5px;
            font: bold 20px/50px Arial;
        }
        /* 存在href属性的元素 */
        .demo a[href] {
            background: pink;
        }
        /* 存在id的元素 */
        .demo a[id] {
            background: red;
        }
        /* 存在title属性的元素 */
        .demo a[title] {
            background: yellow;
        }
        /* 存在target属性的元素 */
        .demo a[target] {
            background: green;
        }
        /* class中包含links的元素 */
        .demo a[class*="class_test"] {
            background: orange;
        }
        /* herf 以 http 开头的元素 */
        .demo a[href^="/"] {
            background: gray;
        }
        /* href 以 .pdf 结尾的元素 */
        .demo a[href$=".doc"] {
            background: black;
        }
    </style>
</head>
<body>

<p class="demo">
    <a href="http://www.baidu.com" class="links item first" id="first">1</a>
    <a href="" class="links item active" target="_blank" title="test1">2</a>
    <a href="img/1.png" class="links item" title="test2">3</a>
    <a href="img/2.html" class="links item class_test">4</a>
    <a href="img/3.jpg" class="links item">5</a>
    <a href="/4.pdf" class="links item">6</a>
    <a href="5.doc" class="links item">7</a>
    <a href="6.ppt" class="links item last">8</a>
    <a class="links item2">9</a>
</p>

</body>
```

![image-20230513210311830](https://s2.loli.net/2023/05/13/aN4z5gOdYfSy8oP.png)

> = 绝对等于
>
> *= 包含这个元素
>
> ^= 以这个开头
>
> $= 以这个结尾

## 美化网页信息

### 美化需求

> 1. 有效的传递页面信息
> 2. 美化网页，页面漂亮才能吸引客户
> 3. 凸显页面的主题
> 4. 提高用户的体验

### span标签

- 重点要突出的字，使用span标签套起来
- 约定俗成

```html
<head>
    <meta charset="UTF-8">
    <title>span标签</title>
    <!--  span 标签: 约定俗成的重点标记 -->
    <style>
        span {
            color: red;
            background: green;
        }
    </style>
</head>
<body>
<p>hello world! <span>Bayyys</span></p>
</body>
```

### 字体样式

> font-family：字体系列
> font-size：字体大小
> font-weight：字体粗细

```html
 <style>
     <!-- oblique - 字体风格 -->
     p{
         font: oblique bolder 12px "楷体";
     }
	body{
		font-family:楷体;
		color：red;
	}
	h1{
		font-size： 50px;
}
	.p1{
		font-weight：blod;
	
	}
</style>
```

### 文本样式

- 颜色 –> color, rgb，rgba
- **文本对齐方式 –> text-align：center**
- **首行缩进 –> text-indent：2em**
- 行高 –> line-height：300px；**单行文字上下居中！line-height = height**
- 下划线 –> text-decoration
- 文本图片水平对齐：vertical-align: middle;

```html
<!--
	颜色：
        单词：#FFFFFF
        RGB：0~F ,rgb(0,255,255)
        RGBA：A（透明度）：0~1,rgba(0,255,255,0.9)
        
    text-indent：段落首行缩进
    line-height: 300px;
    	行高 和 块的高度一致，就可以上下居中
-->

text-decoration:underline/*下划线*/
text-decoration:line-through/*中划线*/
text-decoration:overline/*上划线*/
text-decoration:none/*超链接去下划线*/

<!-- 水平对齐 -->
img,span{vetical-align:middle}/*图片、文字水平对齐 - 垂直对齐  middle中间*/

<p>
    <img src="1.png">
    <span>123124124</span>
</p>
```

### 超链接伪类

```html
<head>
    <meta charset="UTF-8">
    <title>超链接伪类</title>
    <style>
        /* 默认的状态 */
        a {
            text-decoration: none;
            color: black;
        }
        /* 鼠标悬浮的状态(通常只适用这个) */
        a:hover {
            text-decoration: underline;
            color: red;
        }
        /* 鼠标点击的状态 */
        a:active {
            text-decoration: line-through;
            color: green;
        }
        /* 已经访问过的状态 */
        a:link {
            text-decoration: none;
            color: blue;
        }
        /* 鼠标点击后的状态 */
        a:visited {
            text-decoration: none;
            color: yellow;
        }
        /* 阴影: 水平阴影 垂直阴影 模糊距离 阴影颜色 */
        #price {
            text-shadow: 5px 5px 5px red;
        }
    </style>
</head>
<body>

<a href="#">
    <img src="images/book.jpg" alt="">
</a>
<p>
    <a href="#">&lt;this book&gt;</a>
</p>
<p>
    <a href="">作者: HIS</a>
</p>
<p id="price">
    ￥99
</p>
</body>
```

### 列表

- 列表前标志

  - `list-style`

    -  none: 无序列表前面没有任何标志

    -  disc: 默认值，实心圆

    -  circle: 空心圆

    -  square: 实心方块

    -  decimal: 数字

    -  decimal-leading-zero: 0开头的数字

    -  lower-roman: 小写罗马数字

    -  upper-roman: 大写罗马数字

    -  lower-alpha: 小写英文字母

    -  upper-alpha: 大写英文字母

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>列表样式</title>
    <link rel="stylesheet" href="css/style.css" type="text/css">
</head>
<body>

<div id="nav">
    <h2 class="title">全部商品分类</h2>
    <ul>
        <li><a href="#">图书</a>&nbsp;&nbsp;<a href="#">音像</a>&nbsp;&nbsp;<a href="#">数字商品</a></li>
        <li><a href="#">家用电器</a>&nbsp;&nbsp;<a href="#">手机</a>&nbsp;&nbsp;<a href="#">数码</a></li>
        <li><a href="#">电脑</a>&nbsp;&nbsp;<a href="#">办公</a></li>
        <li><a href="#">家居</a>&nbsp;&nbsp;<a href="#">家装</a>&nbsp;&nbsp;<a href="#">厨具</a></li>
        <li><a href="#">服饰鞋帽</a>&nbsp;&nbsp;<a href="#">个护化妆</a></li>
        <li><a href="#">礼品箱包</a>&nbsp;&nbsp;<a href="#">钟表</a>&nbsp;&nbsp;<a href="#">珠宝</a></li>
        <li><a href="#">食品饮料</a>&nbsp;&nbsp;<a href="#">保健食品</a></li>
        <li><a href="#">彩票</a>&nbsp;&nbsp;<a href="#">旅行</a>&nbsp;&nbsp;<a href="#">充值</a>&nbsp;&nbsp;<a
                href="#">票务</a></li>
    </ul>
</div>

</body>
</html>
```

```css
#nav{
    width: 275px;
    background: gray;
}


.title{
    font-size: 18px;
    font-weight: bold;
    text-indent: 1em;
    line-height: 35px;
    background: red;
}

/* ul li */
/*
list-style
    none: 无序列表前面没有任何标志
    disc: 默认值，实心圆
    circle: 空心圆
    square: 实心方块
    decimal: 数字
    decimal-leading-zero: 0开头的数字
    lower-roman: 小写罗马数字
    upper-roman: 大写罗马数字
    lower-alpha: 小写英文字母
    upper-alpha: 大写英文字母
*/
ul{
    background: gray;
}

ul li{
    height: 30px;
    list-style: none;
    text-indent: 1em;
}

/* a */
a{
    text-decoration: none;
    color: #000;
    font-size: 14px;
}

a:hover{
    color: orange;
    text-decoration: underline;
}
```

![image-20230515212852306](https://s2.loli.net/2023/05/15/NQ3aEwJ25BfTdSK.png)

### 背景

1. 背景颜色：background
1. 背景透明度：opacity
2. 背景图片

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>背景</title>
    <style>
        div{
            width: 500px;
            height: 200px;
            margin: 10px;
            float: initial;
            border: 1px solid red;
            /* 默认为repeat(水平垂直平铺) */
            background-image: url("images/pic.png");
        }
        .div1{
            /* 水平平铺 */
            background-repeat: repeat-x;
        }
        .div2{
            /* 垂直平铺 */
            background-repeat: repeat-y;
        }
        .div3{
            /* 不平铺 */
            background-repeat: no-repeat;
        }
        .div4{
            /* 水平垂直平铺 */
            background-repeat: repeat;
        }
        .div5{
            /* space(
            background-repeat: space;
        }


    </style>
</head>
<body>
<div></div>
<div class="div1"></div>
<div class="div2"></div>
<div class="div3"></div>
<div class="div4"></div>
<div class="div5"></div>
<div class="div6"></div>
</body>
</html>
```

![image-20230515214616378](https://s2.loli.net/2023/05/15/pAaeDVc1bUmqgd6.png)

```css
.title{
	...
    background: red url("../images/down.png") 250px no-repeat;
}

ul li{
	...
    background-image: url("../images/right.png");
    background-repeat: no-repeat;
    background-position: 210px center;
}
```

![image-20230515214629454](https://s2.loli.net/2023/05/15/mlxirMU1uwpP3Nc.png)

### 渐变

- 网址：https://www.grablent.com
- 径向渐变、圆形渐变

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <!--径向渐变，圆形-->
    <style>
        body{
            background-color: #FFFFFF;
            background-image: linear-gradient(66deg, #FFFFFF 0%, #6284FF 50%, #FF0000 100%);
        }
    </style>
</head>
<body>

</body>
</html>
```

## 盒子模型

### 盒子

> 1. margin：外边距
> 2. padding：内边距
> 3. border：边框

![image-20230515215908045](https://s2.loli.net/2023/05/15/Tj3pLgbCcwteW9Z.png)

### 边框

> border：粗细 样式 颜色
>
> 1. 边框的粗细
> 2. 边框的样式
> 3. 边框的颜色

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <style>
        /*body总有一个默认的外边框margin：0,常见的*/
        /*h1, ul, li, a, body {*/
        /*    margin: 0;*/
        /*    padding: 0;*/
        /*    text-decoration: none;*/
        /*}*/

        /*border:粗细，样式，颜色*/
        #box {
            width: 300px;
            border: 1px solid red;
        }

        h2 {
            font-size: 16px;
            background-color: cornflowerblue;
            line-height: 30px;
            margin: 0px;
        }

        /* form 标签选择器 */
        form {
            background: #008800;
        }

        div:nth-of-type(1) input {
            border: 3px solid black;
        }

        /*div:nth-of-type(2) input {*/
        /*    border: 3px dashed yellow;*/
        /*}*/

        /*div:nth-of-type(3) input {*/
        /*    border: 2px dashed green;*/
        /*}*/
    </style>
</head>
<body>

<div id="box">
    <h2>会员登录</h2>
    <form action="#">
        <div>
            <span>用户名：</span>
            <input type="text">
        </div>
        <div>
            <span>密码：</span>
            <input type="password">
        </div>
        <div>
            <span>邮箱：</span>
            <input type="text">
        </div>

    </form>
</div>

</body>
</html>
```

![image-20230516212934490](https://s2.loli.net/2023/05/16/Zbv8l4NrEWPTOyg.png)

### 外边距

```html
#box {
    width: 300px;
    border: 1px solid red;
    margin: 0 auto;
}
```

![image-20230516212953947](https://s2.loli.net/2023/05/16/V65iT3mIdwRygzu.png)

```html
<!-- left->right->top->bottom -->
margin:0 0 0 0/*分别表示上、右、下、左；从上开始顺时针*/
/*例1：居中*/
margin:0 auto /*auto表示左右自动*/
/*例2：*/
margin:4px/*表示上、右、下、左都为4px*/
/*例3*/
margin:10px 20px 30px/*表示上为10px，左右为20px，下为30px*/
```

- 盒子大小计算方式：`margin+border+padding+内容的大小`

- 常见初始化操作：

  - ```html
    margin:0;
    padding:0;
    text-decoration:none;/*超链接去下划线*/
    ```

### 圆角边框

- border-radius

```html
<!--
    左上 右上 右下 左下，顺时针方向
    -->
<!--
	圆圈： 圆角 = 半径
-->
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        #div1{
            width: 100px;
            height: 100px;
            border: 10px solid red;
            border-radius: 100px;
        }
        #div2{
            width: 100px;
            height: 50px;
            border: 10px solid red;
            border-radius: 100px 100px 0 0;
        }
        #div3{
            width: 50px;
            height: 50px;
            border: 10px solid red;
            border-radius: 100px 0 0 0;
        }
        img{
            border-radius: 100px;
        }
    </style>
</head>
<body>
<div id="div1"></div>
<div id="div2"></div>
<div id="div3"></div>

<img src="images/tx.jpg" alt="">
</body>
</html>
```

### 盒子阴影

- box-shadow

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!--margin：0 auto; 居中
    要求：块元素，块元素有固定宽度-->
    <style>
        img {
            border-radius: 50px;
            box-shadow: 10px 10px 100px yellow;
        }
    </style>
</head>
<body>
<div>
    <div style="width: 500px;display: block;text-align: center ">
        <img src="images/pic.png" alt="">
    </div>
    <img src="images/pic.png" alt="" style="display: block;margin: 0 auto">
</div>
</body>
</html>

```

## 浮动

### 标准文档流

> 块级元素：独占一行 h1~h6 、p、div、 列表…
>
> 行内元素：不独占一行 span、a、img、strong
>
> 注： 行内元素可以包含在块级元素中，反之则不可以。

### display

- display可选参数
  - block：块元素
  - inline：行内元素
  - inline-block：是块元素，但是可以内联，在一行
  - none：消失

#### 基本展示

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!--block 块元素
        inline 行内元素
        inline-block 是块元素，但是可以内联 ，在一行
    -->
    <style>
        div{
            width: 100px;
            height: 100px;
            border: 1px solid red;
            display: inline-block;
        }
        span{
            width: 100px;
            height: 100px;
            border: 1px solid red;
            display: inline-block;
        }
    </style>
</head>
<body>
<div>div块元素</div>
<span>span行内元素</span>
</body>
</html>
```

![image-20230516221902728](https://s2.loli.net/2023/05/16/DmGcfArCaQPY153.png)

#### 导航页展示

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>QQ会员</title>
    <link rel="stylesheet" href="css/style.css"/>
</head>
<body>
<div class="wrap">
    <!--头部-->
    <header class="nav-header">
        <div class="head-contain">
            <a href="" class="top-logo"><img src="images/pic.png" width="145" height="90"/></a>
            <nav class="top-nav">
                <ul>
                    <li><a href="">功能特权</a></li>
                    <li><a href="">游戏特权</a></li>
                    <li><a href="">生活特权</a></li>
                    <li><a href="">会员特权</a></li>
                    <li><a href="">成长体系</a></li>
                    <li><a href="">年费专区</a></li>
                    <li><a href="">超级会员</a></li>
                </ul>
            </nav>
            <div class="top-right">
                <a href="">登录</a>
                <a href="">开通超级会员</a>
            </div>
        </div>
    </header>
</div>
</body>
</html>
```

```css
* {
    padding: 0;
    margin: 0;
}

a {
    text-decoration: none;
}

.nav-header {
    height: 90px;
    width: 100%;
    background: rgba(0, 0, 0, .6);
}

.head-contain {
    width: 1180px;
    height: 90px;
    margin: 0 auto;
    text-align: center;
}

.top-logo, .top-nav, .top-nav li, .top-right {
    height: 90px;
    display: inline-block;
    vertical-align: top;
}

.top-nav {
    margin: 0 48px;
}

.top-nav li {
    line-height: 90px;
    width: 90px;
}

.top-nav li a {
    display: block;
    text-align: center;
    font-size: 16px;
    color: #fff;
}

.top-nav li a:hover {
    color: blue;
}

.top-right a {
    display: inline-block;
    font-size: 16px;
    text-align: center;
    margin-top: 25px;
    border-radius: 35px;
}

.top-right a:first-of-type {
    width: 93px;
    height: 38px;
    line-height: 38px;
    color: #fad65c;
    border: 1px #fad65c solid;
}

.top-right a:first-of-type:hover {
    color: #986b0d;
    background: #fad65c;
}

.top-right a:last-of-type {
    width: 140px;
    height: 40px;
    font-weight: 700;
    line-height: 40px;
    background: #fad65c;
    color: #986b0d;
}

.top-right a:last-of-type:hover {
    background: #fddc6c;
}
```

![image-20230516221812231](https://s2.loli.net/2023/05/16/T4tS1AzqFniywXE.png)

### float

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="css/style.css" type="text/css">
</head>
<body>
<div id="father">
    <div class="layer01"><img src="images/1.png" alt=""></div>
    <div class="layer02"><img src="images/2.png" alt=""></div>
    <div class="layer03"><img src="images/3.png" alt=""></div>
    <div class="layer04">
        浮动的盒子可以向左浮动，也可以向右浮动，知道它的外边缘碰到包含或另一个浮动盒子为止
    </div>
</div>
</body>
</html>
```

```css
div{
    margin: 10px;
    padding: 5px;
}
#father{
    border: 1px #000 solid;
}
.layer01{
    border: 1px #F00 dashed;
    display: inline-block;
    float: left;/*向左浮动*/
    clear: both;/*清楚浮动*/
}
.layer02{
    border: 1px #00F dashed;
    display: inline-block;
    float: left;
    clear: both;
}
.layer03{
    border: 1px #060 dashed;
    display: inline-block;
    float: left;
    clear: both;
}
.layer04{
    border: 1px #666 dashed;
    font-size: 12px;
    line-height: 23px;
    float: left;
    clear: both;
}
```

![image-20230516222645852](https://s2.loli.net/2023/05/16/hoMKipSvItDJXzl.png)

### overflow及父级边框塌陷问题

- clear
  - right：右侧不允许有浮动元素
  - left：左侧不允许有浮动元素
  - both：两侧不允许有浮动元素
  - none

#### 增加父级元素的高度

```html
#father{
    border: 1px #000 solid;
    height: 800px;
}
```

#### 增加一个空的div标签

- ```html
  <div class = "clear"></div>
  
  <style>
  	.clear{
  		clear:both;
  		margin:0;
  		padding:0;
  }
  </style>
  ```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="css/style.css" type="text/css">
</head>
<body>
<div id="father">
    <div class="layer01"><img src="images/1.png" alt=""></div>
    <div class="layer02"><img src="images/2.png" alt=""></div>
    <div class="layer03"><img src="images/3.png" alt=""></div>
    <div class="layer04">
        浮动的盒子可以向左浮动，也可以向右浮动，知道它的外边缘碰到包含或另一个浮动盒子为止
    </div>
    <div class="clear"></div>
</div>
</body>
</html>
```

```css
div{
    margin: 10px;
    padding: 5px;
}
#father{
    border: 1px #000 solid;
    height: 800px;
}
.layer01{
    border: 1px #F00 dashed;
    display: inline-block;
    float: left;/*向左浮动*/
}
.layer02{
    border: 1px #00F dashed;
    display: inline-block;
    float: left;
}
.layer03{
    border: 1px #060 dashed;
    display: inline-block;
    float: right;
}
/*
    clear：right；右侧不允许有浮动元素
    clear：left； 左侧不允许有浮动元素
    clear：both； 两侧不允许有浮动元素
    clear：none；
 */
.layer04{
    border: 1px #666 dashed;
    font-size: 12px;
    line-height: 23px;
    display: inline-block;
    float: right;
    clear: left;
}
.clear{
    clear: both;
    margin: 0;
    padding: 0;
}
```

#### 父级元素overflow：hidden

- ```html
  overflow: hidden/*隐藏*/
  overflow: scoll/*滚动*/
  ```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <style>
        #content{
            width: 200px;
            height: 150px;
            overflow: scroll;
        }
    </style>
</head>
<body>

<div id="content">
    <img src="images/1.png" alt="">
    <p>
        某雌性生物醉倒在草地上，路人对其上下其手，并在草地上翻滚，一番折腾后某雌性生物迷迷糊糊醒来步履蹒跚地离开了
    </p>
</div>
</body>
</html>
```

#### 父类添加一个伪类:after

- ```html
  #father:after{
  	content:'';
  	display:block;
  	clear:both;
  }
  ```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
    	div{
            margin: 10px;
            padding: 5px;
        }
        #father{
            border: 1px #000 solid;
        }
        #father:after{
            content: '';
            display: block;
            clear: both;
        }
        .layer01{
            border: 1px #F00 dashed;
            display: inline-block;
            float: left;/*向左浮动*/
        }
        .layer02{
            border: 1px #00F dashed;
            display: inline-block;
            float: left;
        }
        .layer03{
            border: 1px #060 dashed;
            display: inline-block;
            float: right;
        }
        /*
        clear：right；右侧不允许有浮动元素
        clear：left； 左侧不允许有浮动元素
        clear：both； 两侧不允许有浮动元素
        clear：none；
         */
        .layer04{
            border: 1px #666 dashed;
            font-size: 12px;
            line-height: 23px;
            display: inline-block;
            float: right;
        }
    </style>
</head>
<body>
<div id="father">
    <div class="layer01"><img src="../lesson06/images/1.png" alt=""></div>
    <div class="layer02"><img src="images/2.png" alt=""></div>
    <div class="layer03"><img src="images/3.png" alt=""></div>
    <div class="layer04">
        浮动的盒子可以向左浮动，也可以向右浮动，知道它的外边缘碰到包含或另一个浮动盒子为止
    </div>
    <div class="clear"></div>
</div>
</body>
</html>
```

#### 总结

> 1. 浮动元素增加空div----》简单、代码尽量避免空div
> 2. 设置父元素的高度-----》简单，元素假设没有了固定的高度，就会超出
> 3. overflow----》简单，下拉的一些场景避免使用
> 4. 父类添加一个伪类:after（推荐）----》写法稍微复杂，但是没有副作用，**推荐使用**

### display与float对比

1. **display：**方向不可以控制
2. **float：**浮动起来的话会脱离标准文档流，所以要解决父级边框塌陷的问题。

## 定位

### 相对定位

- `position: relative; 相对定位 上下左右`

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>相对定位</title>
    <!-- 相对定位
      1. 会相对于自己原来的位置进行移动
      2. 不会影响其他元素的位置
      3. 不会脱离文档流
      4. 会在原来的位置留下一个空白的位置
      5. 可以使用left、right、top、bottom属性进行移动
      6. 可以使用z-index属性进行层级控制
      -->
    <style>
        body {
            padding: 20px;
        }

        div {
            margin: 10px;
            padding: 5px;
            font-size: 12px;
            line-height: 25px;
        }

        .father {
            border: 1px solid #666;
        }

        #first {
            border: 1px dashed red;
            background-color: yellow;
            position: relative;
            top: 20px;
        }

        #second {
            border: 1px dashed blue;
            background-color: green;
            position: relative;
            left: 20px;
        }

        #third {
            border: 1px dashed orange;
            background-color: pink;
            position: relative;
            bottom: 20px;
        }

    </style>
</head>
<body>
<div class="father">
    <div id="first">第一个盒子</div>
    <div id="second">第二个盒子</div>
    <div id="third">第三个盒子</div>
</div>

</body>
</html>
````

![image-20230516231341132](https://s2.loli.net/2023/05/16/Q1cFwVPrg8XiBL5.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>practice</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            text-decoration: none;
        }

        body {
            padding: 20px;
        }

        .father {
            width: 300px;
            height: 300px;
            border: 5px solid pink;
            text-align: center;
            margin: 0 auto;
        }

        a {
            width: 100px;
            height: 100px;
            background-color: mediumpurple;
            line-height: 100px;
            text-align: center;
            color: whitesmoke;
            display: block;
        }

        a:hover {
            background-color: #986b0d;
        }

        #two, #four {
            position: relative;
            left: 200px;
            top: -100px;
        }

        #five {
            position: relative;
            left: 100px;
            top: -300px;
        }
    </style>
</head>
<body>
<div class="father">
    <a href="#" id="one">链接1</a>
    <a href="#" id="two">链接2</a>
    <a href="#" id="three">链接3</a>
    <a href="#" id="four">链接4</a>
    <a href="#" id="five">链接5</a>
</div>
</body>
</html>
```

![image-20230516231406124](https://s2.loli.net/2023/05/16/7k8yiO3THzrAR5E.png)

### 绝对定位

- 相对定位，基于：
  - 没有父级元素定位的前提下，相对于浏览器定位
  - 假设父级元素存在定位，我们通常会相对于父级元素进行偏移
  - 在父级元素范围内移动
- 总结：相对一父级或浏览器的位置，进行指定的偏移，绝对定位的话，它不在标准文档流中，原来的位置不会被保留

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>绝对定位</title>
    <!-- 绝对定位 -->
    -->
    <style>
        div {
            margin: 10px;
            padding: 5px;
            font-size: 12px;
            line-height: 25px;
        }

        #father {
            border: 1px solid #666;
            padding: 0;
            position: relative;
        }

        #first {
            background-color: #a13d30;
            border: 1px dashed #b27530;

        }

        #second {
            background-color: green;
            border: 1px dashed #0ece4f;
            position: absolute;
            right: 30px;
            top: 30px
        }

        #third {
            background-color: red;
            border: 1px dashed #ff1b87;
        }
    </style>
</head>
<body>
<div id="father">
    <div id="first">第一个盒子</div>
    <div id="second">第二个盒子</div>
    <div id="third">第三个盒子</div>
</div>
</body>
</html>
```

![image-20230516231529803](https://s2.loli.net/2023/05/16/neTrADMNhHkxz5i.png)

### 固定定位

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body {
            height: 1000px;
        }

        div:nth-of-type(1) {
            /*绝对定位：没有相对的父级元素，所以相对于浏览器*/
            width: 100px;
            height: 100px;
            background: red;
            position: absolute;
            right: 0;
            bottom: 0;
        }

        div:nth-of-type(2) {
            width: 50px;
            height: 50px;
            background: yellow;
            position: fixed;
            right: 0;
            bottom: 0;
        }
    </style>
</head>
<body>

<div>div1</div>
<div>div2</div>
</body>
</html>
```

![image-20230522211113374](https://s2.loli.net/2023/05/22/6V7mG5JiuspIhc1.png)

### Z-index

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>z-index</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="content">
    <ul>
        <li><img src="images/2.png" alt=""></li>
        <li class="tiptext">study</li>
        <li class="tipBg"></li>
        <li>时间：2023.1.1</li>
        <li>地点：火星</li>
    </ul>
</div>
</body>
</html>
```

```css
#content {
    width: 380px;
    /*padding: 0px;*/
    /*margin: 0px;*/
    overflow: hidden;
    font-size: 12px;
    line-height: 25px;
    border: 1px solid black;
}

ul, li {
    padding: 0px;
    margin: 0px;
    list-style: none;
}

#content ul {
    position: relative;
}

.tiptext, .tipBg {
    position: absolute;
    width: 380px;
    height: 25px;
    top: 90px;
}

.tiptext {
    z-index: 999;
}

.tipBg {
    background-color: white;
    opacity: 0.7;   /* 透明度 */
    /*filter: alpha(opacity=70);  !* IE8及以下 *!*/
}

```

![image-20230522212550009](https://s2.loli.net/2023/05/22/5MvqAK39nkotIgx.png)

## 动画


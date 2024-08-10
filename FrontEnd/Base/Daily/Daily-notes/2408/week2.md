---
title: 2024-08-week2 每日汇总
tags: ['基础' 'JS' 'CSS']
---

## 视频文字特效

> `CSS`

```html
<div class="container">
  <video src="./assets/video.mp4" autoplay muted loop></video>
  <div class="txt">
    <span>视频文字</span>
  </div>
</div>
```

- css 样式
  - 混合模式下: 黑色显示/白色隐藏
  - 从而文字部分显示为背景视频, 其余部分隐藏

```css
.txt {
  background: #fff;
  mix-blend-mode: screen;
}
```

## 函数签名

> `JS`

- JS 语言中指代: **函数名 + 参数列表 + 返回值**

- 函数的实现过程
  1. 设计 -> 函数签名: 供设计实现思路 + 供使用者方便识别
  2. 实现 -> 书写代码

## 图片九宫格

> `CSS`

- 使用伪类选择器 `nth-child` 进行快捷的设置

```html
<div class="container">
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
</div>
```

```css
.container {
  width: 300px;
  height: 300px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.item {
  transition: 0.3s;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  position: relative;
  background-image: url(./assets/photo.jpg);
}

.item:nth-child(3n + 1) {
  left: -20px;
  background-position-x: 0;
}

.item:nth-child(3n + 2) {
  background-position-x: -100px;
}

.item:nth-child(3n) {
  left: 20px;
  background-position-x: -200px;
}

.item {
  top: 20px;
  background-position-y: -200px;
}

.item:nth-child(-n + 6) {
  top: 0;
  background-position-y: -100px;
}

.item:nth-child(-n + 3) {
  top: -20px;
  background-position-y: 0;
}

.container:hover .item {
  left: 0;
  top: 0;
  box-shadow: 0 0 0 rgba(0, 0, 0, 0.5);
}

```

<img src="https://bitiful.bayyys.cn/notes/mac/2024/08/%E6%9C%AA%E5%91%BD%E5%90%8D---01-1723322037.gif" alt="未命名 - 01" style="zoom:33%;" />

## 函数的二义性

> `JS`

- 函数调用可以通过 `func();` 或者 `new func();`
  - ES6 后通过构造函数进行编写需要转换为 `class`
  - 非构造函数可以通关 `new.target` 进行提示

```js
function func() {
	if (new.target) {
		throw new Error("can't invoke with 'new'");
	}
}

new func();	// can't invoke with 'new'
```

## JS 中的可迭代属性

> `JS`

> 使 `var [a, b] = { a: 1, b: 2};` 成立

- js 中实现可迭代属性 `[Symbol.iterator]:function(){}` 可以进行解构, 否则会报错 `intermediate value`

<img src="https://bitiful.bayyys.cn/notes/mac/2024/08/image-20240811044051727-1723322451.png" alt="image-20240811044051727" style="zoom:50%;" />

```js
Object.prototype[Symbol.iterator] = function(){
    return Object.values(this)[Symbol.iterator]();
}
```

<img src="https://bitiful.bayyys.cn/notes/mac/2024/08/image-20240811044815707-1723322895.png" alt="image-20240811044815707" style="zoom:50%;" />

<img src="https://bitiful.bayyys.cn/notes/mac/2024/08/image-20240811045008336-1723323008.png" alt="image-20240811045008336" style="zoom:50%;" />

## null 和 undefined 的区别

> `JS`

- `null` **No Object**
- `undefined` **No Value**

> JS之父 **BrendanEich** 公开承认过 `null` 存在设计缺陷
>
> - `null` 和 `objects` 共享了同一套类型的标记
>   - `typeof null -> object`

## 判断两个对象是否相同

> `JS`

- 以 vue 中的 `hasChanged` 为例

```js
export function hasChanged(x, y) {
  if (x === y) {
    // 排除 +0/-0 的情形
    // 1/+0 -> Infinity
    // 1/-0 -> -Infinity
    return x === 0 && 1 / x !== 1 / y;
  } else {
    // 排除 NaN === NaN -> false 的情形
    return x === x || y === y;
  }
}
```

## 可组合的散列数值

> `JS`

```js
const CREATE = 0b001;
const DELETE = 0b010;
const UPDATE = 0b100;

// 组合权限
const res = CREATE | DELETE;	// -> 0b011

// 判断权限
if ((req & DELETE) === DELETE) ...

// 删除权限
const res = old ^ DELETE
```

## 标记模板字符串

> `JS`

- ES6 标记模板字符串可以简易使用 **字符串+变量** 的配合
- 同时在字符串前可以添加标记实现自定义功能

```js
const name = 'bayyy';
const age = 18;
const str = tag`my name is ${name}, I'm ${age}.`;

function tag() {
  console.log(arguments)
}
// [Arguments] {
// '0': ['my name is ', ", I'm ", "."],
// '1': 'bayyy',
// '2': 18
//	}
```

- 使用示例: 实现 DOM 元素的生命式编程	
  - React: **styled-components**

```js
a.styles`
	color: ${color};
`.content`
	示例文字: ${标记模板字符串}
`

HTMLElement.prototype.styles = function() {
  const styles = generatesString(arguments);
  let curStyle = this.getAttribute('style');
  if (curStyle) {
    curStyle += styles;
  } else {
    curStyle = styles;
  }
  this.style = curStyle;
  return this;
}

// ...
```


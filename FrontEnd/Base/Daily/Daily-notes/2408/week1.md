---
title: 08/07/2024 每日汇总
tags: ['基础' 'JS']

---

## 函数防抖

> `基础` `JS`

```ts
// 防抖函数
const debounce = (fn, delay) => {
  let timer = null;
  return function () {
    clearTimeout(timer);
    timer = setTimeout(fn, delay);
  };
};

// 窗口尺寸改变的加载
window.onresize = debounce(() => {
  console.log("resize");
}, 500);
```

> 窗口时间监听的方式

```ts
window.onresize = func
window.addEventListener('resize', func)
```

## JS 动画

> `JS`

> - JS 动画的绘制过程
>
>   - 理想情况在均匀的渲染帧进行渲染，但实际上渲染间隙并不相等
>     - 其他问题: JS 单线程的时间循环存在问题; 切换 tab 计时出现问题; 忽略清楚计时器
>
>   - 解决方法：使用 H5 新API`requestAnimationFrame()`

```js
function raf() {
  requestAnimationFrame(() => {
    // 设置动画, 使得每次刷新都会执行
    // ...
    raf(); // 递归调用, 需要进行动画结束的判断
  });
}
```

## HTML 元素获取集合

> `基础` `HTML`

- `HTMLCollection` 动态 (getElementsByClassName)
- `NodeList` 静态 (querySelectorAll)

```js
// 实现添加列表
btn?.addEventListener("click", function () {
  const list = document.getElementsByClassName("list")[0];
  console.log(list);
  const items = document.querySelectorAll(".item");
  console.log(items);
  for (let i = 0; i < items.length; i++) {
    const copy = items[i].cloneNode(true);
    list?.appendChild(copy);
  }
});
```

![image-20240808000427598](https://bitiful.bayyys.cn/notes/mac/2024/08/image-20240808000427598-1723046667.png)

## 正则表达式区分 1000…

> `reg` `基础`

> 将 `10000000000` 转换为 `10_000_000_000`

```js
const str = "100000000000";
const result = str.replace(/\B(?=(\d{3})+\b)/g, "_");
```

## CSS 平滑滚动

> `CSS`

- C3 特性
  - `scroll-behavior: smooth` 平滑滚动
- JS 实现滚动
  - `{ele}.scrollTo(x-coord, y-coord)`
  - `{ele}.scrollTo({top?: xxx, left?: xxx, behavior?:['smooth'|'instant'|'auto']})`

## 动画间隔 steps

> `CSS`

- 动画间隔
  - `animation: run 10s steps(10)` 将整个动画间隔分割为 10 份, 且均匀执行

## 原型链 prototype

> `基础`

![image-20240808001808815](https://bitiful.bayyys.cn/notes/mac/2024/08/image-20240808001808815-1723047488.png)

## 动画暂停/启动

> `CSS`

- `animation-play-state: paused/running`

- 组合属性 `animation: rotate 10s linear paused infinite`

- 结合鼠标操作

```CSS
.container {
  animation: rotate 10s linear paused infinite;
}
.container:hover {
  animation-play-state: running;
}
```

## 粘性定位

> `CSS`

```CSS
position: sticky;
top: 0;
```

- 粘性定位以祖先元素的首个 `overflow` 属性元素的相对距离
  - 若均未设置, 则相对视口

##  文本溢出处理

> `CSS`

- 单行文本

```CSS
.single-line {
  width: 200px;
  height: 300px;
  --------------
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

- 多行文本 (css 实现)

```css
.multi-line {
  width: 200px;
  height: 150px;
  line-height: 30px;
  ------------------
  overflow: hidden;							// 超出隐藏
  display: -webkit-box;					// 需要额外显示省略号的展示模式
  -webkit-line-clamp: 5;				// 指定行数 (根据行高和高度判断)
  -webkit-box-orient: vertical;	// 文字排版方向 (使添加省略号)
}
```


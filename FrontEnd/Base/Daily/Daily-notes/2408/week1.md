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
  - 粘性定位必须配合 top/bottom/left/right 使用

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

## 手写 call 方法

> `基础` `JS`

```js
/**
 * 手写 call 方法
 * 不得使用 apply、bind 辅助
 */

Function.prototype.myCall = function (ctx, ...args) {
  ctx = ctx || globalThis;
  const key = Symbol();
  Object.defineProperty(ctx, key, {
    value: this,
    enumerable: false,
  });
  ctx[key] = this;
  const res = ctx[key](...args);
  delete ctx.fn;
  return res;
};

function method(a, b) {
  console.log(this, a, b);
  return a + b;
}

method.myCall({}, 1, 2); // {} 1 2
```

## 取消事件的默认行为

> `HTML`

```js
window.addEventListener('wheel', wheelHandler, {
  passive: false,
});
```

- `addEventListener()` 的第三个参数可以指明监控行为的严格行为
  - 若为 `false` 则表明通知浏览器, 需要监控 `wheel` 的行为
  - 且此时浏览器会降低一定的优化

## 获取 DOM 元素的尺寸

> `HTML`

| 计算方式                   | 说明                           | 解释                         |
| -------------------------- | ------------------------------ | ---------------------------- |
| `clientWidth/clientHeight` | 边框以内的尺寸, 四舍五入的整数 | 视口高度(不含滚动条)         |
| `offsetWidth/offsetHeight` | 布局尺寸, 四舍五入的整数       | 包含滚动条                   |
| `scrollWidth/scrollHeight` | 内容尺寸, 四舍五入的整数       | 含内边距, 包含超出视口的部分 |
| `getBoundingClientRect()`  | 最小矩形尺寸, 包含小数         | 矩形为横平竖直的包含内容     |



<img src="https://bitiful.bayyys.cn/notes/mac/2024/08/image-20240808235324299-1723132404.png" alt="image-20240808235324299" style="zoom:50%;" />

<img src="https://bitiful.bayyys.cn/notes/mac/2024/08/image-20240808235343440-1723132423.png" alt="image-20240808235343440" style="zoom:50%;" />

<img src="https://bitiful.bayyys.cn/notes/mac/2024/08/image-20240808235410296-1723132450.png" alt="image-20240808235410296" style="zoom:50%;" />

<img src="https://bitiful.bayyys.cn/notes/mac/2024/08/image-20240808235432853-1723132472.png" alt="image-20240808235432853" style="zoom:50%;" />

## 监听元素重叠的 API

> `HTML` `JS`

- 监听元素重叠 (如: 监听加载动画是否出现在视口内)
  - 该需求使用滚动条监听, 触发检测太过频繁
  - 使用 `IntersectionObserver` 进行重叠监测

```js
const loading = document.querySelector(".loading");

// 创建一个观察者
const observer = new IntersectionObserver(
  (entries) => {
    if (entries[0].isIntersecting) {
      // 可以识别进入/离开视窗
      console.log("loading is intersecting");
    }
  }, // entries 是一个数组，包含所有被观察的元素
  {
    threshold: 0.5, // 交叉比例
  }
);

// 开始监听
observer.observe(loading); // 无第二个参数，表示监听整个视窗
// observer.observe(...)  // 可以监听多个元素
```

## 监听页面是否可见

> `JS`

```js
window.addEventListener('visibilitychange', () => {
  if (doc.visibilityState === 'hidden') {
    console.log('页面隐藏了...');
  }
}}
```

## 排序思路 Filp

> `JS`

- Flip 动画解决方案
  - F: First 记录起始位置
  - L: Last 记录结束位置
  - I: Invert 反转元素到起始位置
  - P: Play  播放动画回到结束位置

## 监听事件只触发一次

> `HTML`

```js
window.addEventListener('...', ()=>{}, {
  once: true,
})
```

## CSS 保持宽高比

> `CSS`

- `aspect-ratio: w/h` 宽高比

---
title: 2024-09-week4 每日汇总
tags: ['Daily' 'JS' 'CSS']
---

## 闭包漏洞

```js
var o = (function () {
  var obj = {
    a: 1,
    b: 2,
  };
  return {
    get: function (k) {
      return obj[k];
    },
  };
})();

// 不修改代码情况下, 修改 obj 对象
```

### o.get(‘valueOf’)

- 对象除本身成员外, 也可以访问其原型上的成员 (*Oject.prototype*)
  - 例如: `o.get('obj') -> {a:1, b:2}`
- 可以通关 `valueOf` 进行值的查询
  - `console.log(obj.valueOf()); // { a: 1, b: 2 }`

- 但是不能通过 `o.get('valueOf')()` 进行调用

  - ![image-20240927211306709](https://bitiful.bayyys.cn/notes/mac/2024/09/image-20240927211306709-1727442787.png)

  - 直接使用 `const valueOf = Object.prototpye.valueOf; valueOf();` 也会报该错误
  - 产生原因: **this** 指向问题 - 指向全局 (*strict->undefined*)

### 通过访问器

- 主要解决函数调用过程中的 `this` 指向问题

```js
Object.defineProperty(Object.prototype, "newThis", {
  get: function () {
    return this;
  },
});
const obj2 = o.get("newThis");
obj2.a = "change";
console.log(obj2.a); // change
console.log(o.get("a")); // change
```

### 漏洞避免

- 在组件库设计中，避免访问器产生的漏洞

#### 判断是否为已有属性

```js
var o = (function () {
  var obj = {
    a: 1,
    b: 2,
  };
  return {
    get: function (k) {
      // 判断是否拥有该属性
      if (obj.hasOwnProperty(k)) {
        return obj[k];
      }
      return undefined;
    },
  };
})();
```

#### 截断原型

```js
var o = (function () {
  var obj = {
    a: 1,
    b: 2,
  };
  // 使 obj 对象的原型指向 null, 防止原型链上的属性被访问
  Object.setPrototypeOf(obj, null);
  return {
    get: function (k) {
      // if (!obj.hasOwnProperty(k)) {
      //   return undefined;
      // }
      return obj[k];
    },
  };
})(); 
```

## for-in 循环 (属性描述符)

```js
var obj = { a: 1, b: 2 };

Object.prototype.c = 3;

for (var key in obj) {
  console.log(key); // a, b, c
}

// 添加在原型链上的何种属性会被 for-in 循环遍历到？
```

- 因为不同属性的 **属性描述符** 

```js
var desc = Object.getOwnPropertyDescriptor(Object.prototype, "c");
console.log(desc); // { value: 3, writable: true, enumerable: true, configurable: true }
// writable: 可以修改属性的值
// enumerable: 可以被遍历
// configurable: 可以修改属性的描述符
```

- 定义属性中修改 **属性描述符**

```js
Object.defineProperty(Object.prototype, "d", {
  value: 4,
  writable: true,
  enumerable: false,
  configurable: true,
});

for (var key in obj) {
  console.log(key); // a, b, c
}
```

## flex 弹性盒均分布局

### 空内容

- `flex-grow: 1;` 均分剩余空间
  - 注意：均分 **可用空间**，且会根据已有尺寸进行比例均分

```html
<head>
  <style>
    .root {
      display: flex;
      width: 100%;
      height: 100vh;
    }
    .part {
      flex-grow: 1;
    }
  </style>
</head>
<body>
  <div class="root">
    <div class="part" style="background-color: #e8685c"></div>
    <div class="part" style="background-color: #f3be50"></div>
    <div class="part" style="background-color: #61c354"></div>
  </div>
</body>
```

![image-20240927214129353](https://bitiful.bayyys.cn/notes/mac/2024/09/image-20240927214129353-1727444489.png)

### 包含内容

- `flex-basis: 0` 基础为 0
  - 复合属性 `flex: 1 0 0`   
  - `拉伸比例 压缩比例 基础比例`

```html
<head>
  <style>
    .root {
      display: flex;
      width: 100%;
      height: 100vh;
    }
    .part {
      flex-grow: 1;
      flex-basis: 0;
    }
  </style>
</head>
<body>
  <div class="root">
    <div class="part" style="background-color: #e8685c">part1</div>
    <div class="part" style="background-color: #f3be50"></div>
    <div class="part" style="background-color: #61c354"></div>
  </div>
</body>
```


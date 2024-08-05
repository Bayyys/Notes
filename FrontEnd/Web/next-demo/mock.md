---
title: 前端 mock 技巧，mock.js 的使用
date: 7/29/2024
updated: 07/29/2024
description: mock 测试是在开发过程中，对于不易构建或不易获取的数据/场景，使用虚拟对象进行数据创建的测试方法。以解决开发不同单元间耦合为目标
tags: ['mock' 'test']
---

## mock 测试

- 一种通过模拟对象行为而不是真实对象来进行测试的方法
  - 通过 Mock 测试，开发者可以模拟**对象、服务或系统组件**的行为，以便在**隔离环境**中对特定功能进行测试
  - Mock 对象可以确保测试的焦点放在代码本身，而不受外部系统的干扰
- 常见用途
  - **隔离依赖**： 当被测系统依赖外部服务、数据库、文件系统等时，使用 Mock 对象可以隔离这些依赖，使得测试更加可控
  - **模拟外部服务**： 当测试系统与外部服务进行交互时，使用 Mock 对象可以模拟这些外部服务的响应，而不必实际调用真实的服务
  - **控制测试场景**： Mock 对象允许开发人员控制测试中的各种场景，例如模拟异常、模拟特定的返回值，以确保系统在各种情况下都能正常工作

## mock.js

> [mock.js](http://mockjs.com/)  生成随机数据, 拦截 Ajax 请求
>
> - 示例: [examples](http://mockjs.com/examples.html)

### 基本使用

```ts
const mock = require("mockjs");

// 140000199412185622
const id = mock.mock("@id");

// { id: '140000199412185622' }
const idObj = mock.mock({
  id: "@id",
});

const obj = mock.mock({
  id: "@id",
  username: "@cname",
  date: "@date",
  avatar: "@image('200x100', '#50B347', '#FFF', 'Avatar')",
  description: "@paragraph",
  ip: "@ip",
  email: "@email",
  url: "@url",
});
console.log("🚀 ~ obj:", obj);
```

### JSON5

- json 存在的问题
  - 不能添加注释
  - 序列化后 key 需要添加引号
- json5 特点
  - 对象与 JS 中对象 key-value 完全一致
  - 支持注释
- 目录结构

![image-20240729232950343](https://upyun.bayyys.cn/notes/mac%252F2024%252F07%252Fimage-20240729232950343-1722266990.png)

```ts
// parseJson5.ts

const fs = require("fs");
const path = require("path");
const json5 = require("json5");

const json = fs.readFileSync(path.join(__dirname, "userInfo.json5"), "utf-8");
const obj = json5.parse(json);
console.log("🚀 ~ obj:", obj);
```

```ts
// userInfo.json5
{
  id: "@id",
  username: "@cname",
  date: "@date",
  avatar: "@image('200x100', '#50B347', '#FFF', 'Avatar')",
  description: "@paragraph",
  ip: "@ip",
  email: "@email",
  url: "@url",
}
```

### 请求拦截

```ts
Mock.mock(rurl, template)
Mock.mock(rurl, function(options))
Mock.mocl(rurl, rtype, template)
Mock.mock(rurl, rtype, function(options))
```

- 参数说明
  - `rurl` 需要拦截的 URL, 可以是 URL 字符串或 URL 正则
  - `rtype` 需要拦截的 AJAX 请求
  - `template` 数据模板, 可以是对象或字符串
  - `function` 用于生成响应数据的函数
- 对 axios 等网络请求进行拦截
- 可以进行环境变量的设置, 使在测试环境中进行 mock

```ts
// ./mock/index.ts

const Mock = require("mockjs");

export const userData = Mock.mock("/user/list", "get", {
  code: 200,
  message: "success",
  "data|2-10": [
    {
      "id|+1": 1,
      username: "@cname",
      date: "@date",
      "age|18-60": 1,
      "sex|1": ["男", "女"],
      "star|1-10": "★",
      "surgery|50-100.1-10": 1,
      avatar: "@image('200x100', '#50B347', '#FFF', 'Avatar')",
      description: "@paragraph",
      ip: "@ip",
      email: "@email",
      url: "@url",
    },
  ],
});
```

- 主函数中直接引入并使用即可

```tsx
import "@/mock/index";
import axios from "axios";

export default function Home() {
  const handlerClick = async () => {
    const res = await axios.get("/user/list");
    console.log("🚀 ~ handlerClick ~ res:", res.data.data);
  };

  return <button onClick={handlerClick}>Click me</button>
}

```

![image-20240729235157394](https://upyun.bayyys.cn/notes/mac%252F2024%252F07%252Fimage-20240729235157394-1722268317.png)

### Mock.setup

```ts
Mock.setup(settings)
```

- 配置拦截 Ajax 请求时的行为
- 支持项
  - `timeout` 超时时间, 经过此段时间后响应, 使用 `-` 可以标识范围, 默认为 `10-100` (ms)

### Mock.Random

- mockjs 的工具类, 用于生成各种随机数据
- 在数据模板中称为 **占位符**, 书写格式为 **@占位符(参数)**

### 正则匹配

- 可以使用正则表达式进行匹配, 以此解析 query 参数

```ts
export const queryData = Mock.mock(/\/data/, "get", (req: any) => {
  const { url, type, body } = req;
  return {
    url,
    type,
    body,
  };
});

// 请求测试
const res = await axios.get("/data?name=张三&age=18");
```

![image-20240731231817715](https://upyun.bayyys.cn/notes/mac%252F2024%252F07%252Fimage-20240731231817715-1722439097.png)

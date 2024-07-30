---
title: xml 格式解析至 JSON
date: 07/30/2024
description: 在实际处理后端返回数据过程中发现部分接口返回为 XML 格式, 需要将其转化为 JSON 进行使用
tags: ['xml' 'json']
---

## xml2js

> [xml2js](https://www.npmjs.com/package/xml2js) XML 到 JavaScript 对象转换器, 支持双向转换

### 简单使用

```ts
// xml 虚拟数据
const xmldata = `
    <root>
      <person>
        <name>zhangsan</name>
        <age>18</age>
      </person>
      <person>
        <name>lisi</name>
        <age>19</age>
      </person>
    </root>`;

const parser = new xml2js.Parser();

const data = parser
.parseStringPromise(xmldata, {
  explicitArray: false, // 不转换为数组
  explicitRoot: false, // 不转换为根节点
})
.then((res: any) => {
  console.log(res);
});
// 也可以 Promise
```

### 参数说明

- `trim` 修剪文本节点开头和结尾的空格
- `normalizeTags` 将所有标签名标准化为小写
- `normilize` 修剪文本节点内的空格
- `explicitRoot` 是否获取根节点

- `emptyTag` 空节点值设置, 默认为 `‘ ’`
- `explicitArray` **false** 时, 仅当存在多个数组时, 创建数组

- …

## DOM 树解析

> [解析或序列化 XML](https://developer.mozilla.org/zh-CN/docs/Web/XML/Parsing_and_serializing_XML)

- 序列化 DOM 树 `XMLSerializer`
- 解析 XML 字符串来构建 DOM 树 `DOMParser`
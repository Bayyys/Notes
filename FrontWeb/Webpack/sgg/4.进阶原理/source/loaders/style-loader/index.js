module.exports = function (content) {
  /*
    1. 直接使用style-loader，只能处理样式
      不能处理样式中引入的其他资源

      use: ["./loaders/style-loader"],

    2. 借助css-loader解决样式中引入的其他资源的问题

      use: ["./loaders/style-loader", "css-loader"],

      问题是css-loader暴露了一段js代码，style-loader需要执行js代码，得到返回值，再动态创建style标签，插入到页面上
      不好操作

    3. style-loader使用pitch loader用法
  */
  // const script = `
  //   const styleEl = document.createElement('style');
  //   styleEl.innerHTML = ${JSON.stringify(content)};
  //   document.head.appendChild(styleEl);
  // `;
  // return script;
};

module.exports.pitch = function (remainingRequest) {
  // remainingRequest 剩下还需要处理的loader
  // console.log(remainingRequest); // C:\Users\86176\Desktop\webpack\source\node_modules\css-loader\dist\cjs.js!C:\Users\86176\Desktop\webpack\source\src\css\index.css

  // 1. 将 remainingRequest 中绝对路径改成相对路径（因为后面只能使用相对路径操作）
  const relativePath = remainingRequest
    .split("!")
    .map((absolutePath) => {
      // 返回相对路径
      return this.utils.contextify(this.context, absolutePath);
    })
    .join("!");

  // console.log(relativePath); // ../../node_modules/css-loader/dist/cjs.js!./index.css

  // 2. 引入css-loader处理后的资源
  // 3. 创建style，将内容插入页面中生效
  const script = `
    import style from "!!${relativePath}";
    const styleEl = document.createElement('style');
    styleEl.innerHTML = style;
    document.head.appendChild(styleEl);
  `;

  // 中止后面loader执行
  return script;
};

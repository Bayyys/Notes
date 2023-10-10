document.getElementById("btn").onclick = function () {
  // 动态导入 --> 实现按需加载
  // 即使只被引用了一次，也会代码分割
  import("./math.js").then(({ sum }) => {
    alert(sum(1, 2, 3, 4, 5));
  });
  // 返回的是一个promise
  import("./math.js")
    .then((res) => {
      console.log("模块加载成功! ", res.sum(1, 2, 3, 4, 5));
    })
    .catch((err) => {
      console.log("模块加载失败! ", err);
    });
};

import count from "./js/count";
// 引入样式
import "./css/index.css";
import "./less/index.less";
import "./sass/index.scss";
import "./sass/index.sass";
import "./stylus/index.styl";
import "./css/iconfont.css";
document.getElementById("btn").onclick = function () {
  // 动态导入 --> 实现按需加载
  // 即使只被引用了一次，也会代码分割
  // eslint会对动态导入语法报错，需要修改eslint配置文件
  // webpackChunkName: "math"：这是webpack动态导入模块命名的方式
  // "math"将来就会作为[name]的值显示。
  import(/* webpackChunkName: "sum" */ "./js/sum").then(({ sum }) => {
    console.log(sum(1, 2, 3, 4, 5));
  });
};
const result1 = count(1, 2);
console.log(result1);

// 判断是否支持HMR功能
if (module.hot) {
  module.hot.accept("./js/count.js");

  module.hot.accept("./js/sum.js");
}

// 完整引入
// import 'core-js'
// 按需加载
// import "core-js/es/promise";

import count from "./js/count";
import sum from "./js/sum";

// 想要webpack打包资源，必须引入该资源
import "./css/iconfont.css";
import "./css/index.css";
import "./less/index.less";
import "./sass/index.sass";
import "./sass/index.scss";
import "./stylus/index.styl";

const result = count(2, 3);
console.log(result);
console.log(sum(1, 2, 3, 4));

document.getElementById("btn").onclick = function () {
  // eslint不能识别动态导入需要，需要额外追加配置
  // webpack魔法命名
  import(/* webpackChunkName: "math", webpackPrefetch: true */ "./js/math").then(({ mul }) => {
    console.log(mul(3, 3));
  });
};

if (module.hot) {
  // 判断是否支持热模块替换功能
  module.hot.accept("./js/count");
  module.hot.accept("./js/sum");
}

new Promise((resolve) => {
  setTimeout(() => {
    resolve();
  }, 1000);
});

const arr = [1, 2, 3, 4];
console.log(arr.includes(1));

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/service-worker.js")
      .then((registration) => {
        console.log("SW registered: ", registration);
      })
      .catch((registrationError) => {
        console.log("SW registration failed: ", registrationError);
      });
  });
}

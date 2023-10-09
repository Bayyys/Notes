import count from "./js/count";
import sum from "./js/sum";

// 想要webpack打包资源，必须引入该资源
import "./css/iconfont.css";
import "./css/index.css";
import "./less/index.less";
import "./sass/index.sass";
import "./sass/index.scss";
import "./stylus/index.styl";

const result = count(2, 2);
console.log(result);
console.log(sum(1, 2, 3, 4));

import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import store from "./redux/store";

ReactDOM.render(<App />, document.getElementById("root"));

// 当store中的状态发生改变时，重新渲染App组件
store.subscribe(() => {
  ReactDOM.render(<App />, document.getElementById("root"));
});

import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { Provider } from "react-redux";
import store from "./redux/store";

ReactDOM.render(
  /* 使用 Provider 包裹 APP, 目的是让App所有的后代容器都能接受到store */
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);

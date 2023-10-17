import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";  // 用于性能分析

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    {" "}
    {/* React 自己的严格模式, 用于检查组件的语法(例如: 字符串类型ref) */}
    <App />
  </React.StrictMode>
);

reportWebVitals(); // 记录页面性能监测数据(会使用 web-vitals 库)

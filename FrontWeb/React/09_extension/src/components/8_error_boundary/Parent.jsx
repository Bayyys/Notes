import React, { Component } from "react";
import Child from "./Child";
import "./index.css";

export default class Parent extends Component {
  state = {
    hasError: "", // 用于标识子组件是否产生错误
  };

  // 若想在组件出错后，不显示错误的组件，而显示自定义的错误界面，需要用到错误边界
  // 当Parent组件的子组件出现报错时，会触发getDerivedStateFromError调用，并携带错误信息
  static getDerivedStateFromError(error) {
    console.log(error);
    // 返回新的state
    return {
      hasError: true,
    };
  }

  // 使用时机: 组件出现错误时, 会触发
  componentDidCatch(error, info) {
    // 统计页面的错误。发送请求发送到后台去
    console.log(error, info);
  }

  render() {
    return (
      <div className="parent">
        <h1>Parent组件</h1>
        {this.state.hasError ? (
          <h1>当前网络不稳定, 请稍后重试...</h1>
        ) : (
          <Child />
        )}
      </div>
    );
  }
}

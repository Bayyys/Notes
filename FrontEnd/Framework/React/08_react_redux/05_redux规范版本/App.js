import React, { Component } from "react";
import { Divider, Space } from "antd";
// 引入的是容器组件
import Count from "./containers/Count";
import People from "./containers/People";

export default class App extends Component {
  render() {
    return (
      <Space direction="vertical">
        <Count />
        <Divider />
        <People />
      </Space>
      
    );
  }
}

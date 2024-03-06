import React, { Component } from "react";
import { Button, DatePicker, Input, ConfigProvider, theme } from "antd";

export default class App extends Component {
  render() {
    return (
      <div>
        <ConfigProvider
          theme={{
            token: {
              // // Seed Token，影响范围大
              // colorPrimary: "#f7afec",
              // borderRadius: 8,

              // // 派生变量，影响范围小
              // colorBgContainer: "#ffedfe",

              algorithm: theme.darkAlgorithm,
            },
          }}
        >
          <h1>APP</h1>
          <Button type="primary">按钮</Button> <br />
          <Input placeholder="Please Input" />
          <DatePicker />
        </ConfigProvider>
      </div>
    );
  }
}

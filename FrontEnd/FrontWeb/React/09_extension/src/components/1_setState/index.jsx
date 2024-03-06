import React, { Component } from "react";

export default class SetStateDemo extends Component {
  state = {
    count: 0,
  };

  add = () => {
    // 1. 对象式的setState
    const { count } = this.state;
    this.setState({ count: count + 1 }, () => {
      console.log(this.state.count); // 获取的是更新后的值
    });
    console.log(this.state.count); // 获取的是更新前的值(异步更新)

    // 2. 函数式的setState
    this.setState((state, props) => {
      return { count: state.count + 1 };
    });

    this.setState((state) => ({ count: state.count + 1 }));
  };

  render() {
    return (
      <div>
        <h1>当前求和为: {this.state.count}</h1>
        <button onClick={this.add}>+1</button>
      </div>
    );
  }
}

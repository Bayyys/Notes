import React, { Component } from "react";
import { Select, Space, Button } from "antd";
import store from "../../redux/store";
import { incrementAction, decrementAction } from "../../redux/count_action";

export default class Count extends Component {
  state = { count: 0, operator: 0 };

  componentDidMount() {
    // 当store中的状态发生改变时，重新渲染组件
    store.subscribe(() => {
      this.setState({});
    });
  }

  increment = () => {
    const { operator } = this.state;
    // store.dispatch({ type: "increment", data: operator }); // 通知redux进行加法运算
    store.dispatch(incrementAction(operator)); // 通知redux Action对象进行加法运算
  };

  decrement = () => {
    const { operator } = this.state;
    // store.dispatch({ type: "decrement", data: operator });
    store.dispatch(decrementAction(operator));
  };

  incrementIfOdd = () => {
    const { operator } = this.state;
    const count = store.getState();
    if (count % 2 === 1) {
      // store.dispatch({ type: "increment", data: operator });
      store.dispatch(incrementAction(operator)); // 通知redux Action对象进行加法运算
    }
  };

  incrementAsync = () => {
    const { operator } = this.state;
    setTimeout(() => {
      // store.dispatch({ type: "increment", data: operator });
      store.dispatch(incrementAction(operator)); // 通知redux Action对象进行加法运算
    }, 500);
  };

  render() {
    return (
      <div>
        <Space direction="vertical" size="large" style={{ display: "flex" }}>
          <h1>当前求和为: {store.getState()}</h1>
          <Select
            onChange={(num) => {
              this.setState({ operator: +num });
            }}
            defaultValue="0"
            style={{ width: 120 }}
            options={[
              { value: "0", label: "0" },
              { value: "1", label: "1" },
              { value: "2", label: "2" },
              { value: "3", label: "3" },
            ]}
          />
          <Space>
            <Button onClick={this.increment}>+</Button>
            <Button onClick={this.decrement}>-</Button>
            <Button onClick={this.incrementIfOdd}>odd+</Button>
            <Button onClick={this.incrementAsync}>Async+</Button>
          </Space>
        </Space>
      </div>
    );
  }
}

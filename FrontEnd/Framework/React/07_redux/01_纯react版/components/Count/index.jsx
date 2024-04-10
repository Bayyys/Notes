import React, { Component } from "react";
import { Select, Space, Button } from "antd";

export default class Count extends Component {
  state = { count: 0, operator: 0 };

  increment = () => {
    const { count, operator } = this.state;
    this.setState({ count: count + operator });
  };

  decrement = () => {
    const { count, operator } = this.state;
    this.setState({ count: count - operator });
  };

  incrementIfOdd = () => {
    const { count, operator } = this.state;
    if (count % 2 === 1) {
      this.setState({ count: count + operator });
    }
  };

  incrementAsync = () => {
    const { count, operator } = this.state;
    setTimeout(() => {
      this.setState({ count: count + operator });
    }, 500);
  };

  render() {
    return (
      <div>
        <Space direction="vertical" size="large" style={{ display: "flex" }}>
          <h1>当前求和为: {this.state.count}</h1>
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

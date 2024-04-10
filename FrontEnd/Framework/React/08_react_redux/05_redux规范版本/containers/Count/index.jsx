import React, { Component } from "react";
import { Select, Space, Button } from "antd";
import { connect } from "react-redux";
import {
  increment,
  decrement,
  incrementAsync,
} from "../../redux/actions/count";

class Count extends Component {
  state = { operator: 0 };

  increment = () => {
    this.props.increment(this.state.operator);
  };

  decrement = () => {
    this.props.decrement(this.state.operator);
  };

  incrementIfOdd = () => {
    if (this.props.count % 2 !== 0) {
      this.props.increment(this.state.operator);
    }
  };

  incrementAsync = () => {
    this.props.incrementAsync(this.state.operator, 1000);
  };

  render() {
    return (
      <div>
        <Space direction="vertical" size="large" style={{ display: "flex" }}>
          <h1>
            当前求和为: {this.props.count}, 总人数为: {this.props.people.length}
          </h1>
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

const mapStateToProps = (state) => ({
  people: state.people,
  count: state.count,
});

const mapDispatchToProps = { increment, decrement, incrementAsync };

export default connect(mapStateToProps, mapDispatchToProps)(Count);

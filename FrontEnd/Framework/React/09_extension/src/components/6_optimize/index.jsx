import React, { PureComponent } from "react";
import "./index.css";

export default class Parent extends PureComponent {
  state = {
    carName: "奔驰c63",
  };

  render() {
    console.log("Parent---render");
    const { carName } = this.state;
    return (
      <div className="parent">
        <h1>Parent组件</h1>
        <span>今天开 {carName}</span> <br />
        <button onClick={() => this.setState({ carName: "Model 3" })}>
          换车
        </button>
        <Child carName={carName} />
      </div>
    );
  }
}

class Child extends PureComponent {
  render() {
    console.log("Child---render");
    return (
      <div className="child">
        <h1>Child组件</h1>
        <span>parent今天开 {this.props.carName}</span>
      </div>
    );
  }
}

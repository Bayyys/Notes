import React, { PureComponent } from "react";
import "./index.css";

export default class Parent extends PureComponent {
  render() {
    return (
      <div className="parent">
        <h1>Parent组件</h1>
        <Child render={(name) => <Grandchild name={name} />} />
      </div>
    );
  }
}

class Child extends PureComponent {
  render() {
    return (
      <div className="child">
        <h1>Child组件</h1>
        {this.props.render("tom")}
      </div>
    );
  }
}

class Grandchild extends PureComponent {
  render() {
    return (
      <div className="grandchild">
        <h1>Grandchild组件</h1>
        <h1>展示的姓名为: {this.props.name}</h1>
      </div>
    );
  }
}

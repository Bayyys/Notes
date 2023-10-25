import React, { Component } from "react";
import "./index.css";

// 1. 创建Context对象
const UsernamContext = React.createContext();
export default class A extends Component {
  state = {
    username: "tom",
    age: 18,
  };
  render() {
    const { username, age } = this.state;
    return (
      <div className="parent">
        <h1>组件A, 用户名为: {username}</h1>
        <UsernamContext.Provider value={{ username, age }}>
          <B />
        </UsernamContext.Provider>
      </div>
    );
  }
}

class B extends Component {
  render() {
    return (
      <div className="child">
        <h1>组件B</h1>
        <C />
        <D />
      </div>
    );
  }
}

class C extends Component {
  static contextType = UsernamContext;
  render() {
    return (
      <div className="grandchild">
        <h1>
          组件C, 接收到的用户名为: {this.context.username}, 年龄:{" "}
          {this.context.age}
        </h1>
      </div>
    );
  }
}

function D() {
  return (
    <div className="grandchild">
      <h1>
        <UsernamContext.Consumer>
          {(value) =>
            `组件D, 接收到的用户名为: ${value.username}, 年龄: ${value.age}`
          }
        </UsernamContext.Consumer>
      </h1>
    </div>
  );
}

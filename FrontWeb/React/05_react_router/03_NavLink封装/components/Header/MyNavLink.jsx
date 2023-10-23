// MyNavLink 组件
import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export default class MyNavLink extends Component {
  render() {
    // this.props.children 可以取到标签内容，如 About, Home
    // 反过来通过指定标签的 children 属性可以修改标签内容
    return (
      <NavLink
        activeClassName="active"
        className="list-group-item"
        {...this.props}
      />
    );
  }
}

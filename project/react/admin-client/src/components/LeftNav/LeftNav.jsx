import React from "react";
import { Link } from "react-router-dom";
import { Menu } from "antd";

import "./LeftNav.css";
import logo from "../../assets/images/logo.png";
import menuList from "../../config/menuConfig";

import { getMenuNodes } from "../../utils/menuUtils";

export default function LeftNav() {
  return (
    <div className="left-nav">
      <Link className="left-nav-header">
        <img src={logo} alt="" />
        <h1>后台管理</h1>
      </Link>
      <Menu
        defaultSelectedKeys={["/home"]} // 默认选中
        defaultOpenKeys={["/products"]} // 默认展开
        mode="inline" // 菜单类型: vertical(垂直) | horizontal(水平) | inline(内嵌)
        theme="dark"
      >
        {getMenuNodes(menuList)}
      </Menu>
    </div>
  );
}

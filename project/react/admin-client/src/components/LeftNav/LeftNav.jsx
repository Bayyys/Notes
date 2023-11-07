import React from "react";
import { Link, useLocation } from "react-router-dom";
import { Menu } from "antd";

import "./LeftNav.scss";
import logo from "../../assets/images/logo.png";
import menuList from "../../config/menuConfig";

import { getMenuNodes } from "../../utils/menuUtils";

export default function LeftNav() {
  let selectKey = useLocation().pathname; // 当前请求的路径
  let openKey = useLocation().pathname.split("/").slice(0, -1).join("/"); // 当前请求的路径的父路径
  if (selectKey.indexOf("/product") === 0) {
    // 当前请求的是商品或其子路由界面
    selectKey = "/product";
    openKey = "/products";
  }

  return (
    <div className="left-nav">
      <Link className="left-nav-header">
        <img src={logo} alt="" />
        <h1>后台管理</h1>
      </Link>
      <Menu
        selectedKeys={[selectKey]} // 当前选中的菜单项 key 数组
        defaultSelectedKeys={[selectKey]} // 默认选中
        defaultOpenKeys={[openKey]} // 默认展开
        mode="inline" // 菜单类型: vertical(垂直) | horizontal(水平) | inline(内嵌)
        theme="dark"
      >
        {getMenuNodes(menuList)}
      </Menu>
    </div>
  );
}

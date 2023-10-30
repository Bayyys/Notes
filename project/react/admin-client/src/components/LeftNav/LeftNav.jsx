import React from "react";
import { NavLink } from "react-router-dom";
import {
  MailOutlined,
  PieChartOutlined,
  ContainerOutlined,
  AppstoreOutlined,
} from "@ant-design/icons";
import { Menu } from "antd";

import "./LeftNav.css";
import logo from "../../assets/images/logo.png";
const { Item, SubMenu } = Menu;

export default function LeftNav() {
  return (
    <div className="left-nav" to="/admin">
      <NavLink className="left-nav-header">
        <img src={logo} alt="" />
        <h1>后台管理</h1>
      </NavLink>
      <Menu
        defaultSelectedKeys={["1"]}
        defaultOpenKeys={["sub1"]}
        mode="inline"
        theme="dark"
        // items={items}
      >
        <Item key="home">
          <PieChartOutlined />
          <span>首页</span>
        </Item>
        <SubMenu
          key="market"
          icon={<ContainerOutlined />}
          title={<span>商品</span>}
        >
          <Item key="tub1-1">
            <MailOutlined />
            <span>品类管理</span>
          </Item>
          <Item key="sub1-2">
            <MailOutlined />
            <span>商品管理</span>
          </Item>
        </SubMenu>
        <Item key="user">
          <PieChartOutlined />
          <span>用户管理</span>
        </Item>
        <Item key="role">
          <PieChartOutlined />
          <span>角色管理</span>
        </Item>
        <SubMenu
          key="charts"
          icon={<AppstoreOutlined />}
          title={<span>图形图表</span>}
        >
          <Item key="sub2-1">
            <MailOutlined />
            <span>柱形图</span>
          </Item>
        </SubMenu>
      </Menu>
    </div>
  );
}

import React from "react";
import { NavLink } from "react-router-dom";
import { MailOutlined, PieChartOutlined } from "@ant-design/icons";
import { Menu } from "antd";
import storageUtils from "./storageUtils";

const { Item, SubMenu } = Menu;

/**
 * 根据menu的数据数组生成对应的标签数组
 * [{
 *  title: '首页', // 菜单标题名称
 *  key: '/home', // 对应的path
 *  icon: 'home', // 图标名称
 *  items: [], // 可能有, 也可能没有
 * }]
 */
export const getMenuNodes_old = (menuList) => {
  return menuList.map((item) => {
    if (!item.children) {
      return (
        <Item key={item.key} icon={<PieChartOutlined />}>
          <NavLink to={item.key}>{item.title}</NavLink>
        </Item>
      );
    } else {
      return (
        <SubMenu key={item.key} icon={<MailOutlined />} title={item.title}>
          {getMenuNodes_old(item.children)}
        </SubMenu>
      );
    }
  });
};

/**
 * 判断当前登录用户对item是否有权限
 * @param {*} item 列表项
 * @returns 有权限返回true，没有权限返回false
 */
function hasAuth(item) {
  const user = storageUtils.getUser();
  if (!user._id) {
    return false;
  }
  const menus = user.role.menus;
  const { key, isPublic } = item;
  // 如果当前用户是admin, 直接返回true
  if (isPublic || user.username === "admin" || menus.indexOf(key) !== -1) {
    return true;
  }
  // 判断是否有item的子item的权限
  else if (item.children) {
    return !!item.children.find((child) => menus.indexOf(child.key) !== -1);
  }
  return false;
}

function getItem(label, key, icon, children, type) {
  return {
    key,
    icon,
    children,
    label,
    type,
  };
}

export const getMenuNodes = (menuList) => {
  return menuList.map((item) => {
    if (!item.children && hasAuth(item)) {
      return getItem(item.title, item.key, <MailOutlined />, null);
    } else {
      if (!hasAuth(item)) {
        return null;
      } else
        return getItem(
          item.title,
          item.key,
          <PieChartOutlined />,
          getMenuNodes(item.children)
        );
    }
  });
};

export const getMunuName = (menuList, path) => {
  let title;
  menuList.forEach((element) => {
    if (path.indexOf(element.key) === 0) {
      title = element.title;
    } else if (element.children) {
      const tmp = getMunuName(element.children, path);
      if (tmp) {
        title = tmp;
      }
    }
  });
  return title;
};

export const getMenuNodes_reduce = (menuList) => {
  return menuList.reduce((pre, item) => {
    if (!item.items) {
      pre.push(
        <Item key={item.key} icon={<PieChartOutlined />}>
          <NavLink to={item.key}>{item.title}</NavLink>
        </Item>
      );
    } else {
      pre.push(
        <SubMenu key={item.key} icon={<MailOutlined />} title={item.title}>
          {getMenuNodes_reduce(item.items)}
        </SubMenu>
      );
    }
    return pre;
  }, []);
};

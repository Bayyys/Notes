import React from "react";
import { NavLink } from "react-router-dom";
import { MailOutlined, PieChartOutlined } from "@ant-design/icons";
import { Menu } from "antd";

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
export const getMenuNodes = (menuList) => {
  return menuList.map((item) => {
    if (!item.items) {
      return (
        <Item key={item.key} icon={<PieChartOutlined />}>
          <NavLink to={item.key}>{item.title}</NavLink>
        </Item>
      );
    } else {
      return (
        <SubMenu key={item.key} icon={<MailOutlined />} title={item.title}>
          {getMenuNodes(item.items)}
        </SubMenu>
      );
    }
  });
};

export const getMunuName = (menuList, path) => {
  let title;
  menuList.forEach((element) => {
    if (path.indexOf(element.key) === 0) {
      title = element.title;
    } else if (element.items) {
      const tmp = getMunuName(element.items, path);
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

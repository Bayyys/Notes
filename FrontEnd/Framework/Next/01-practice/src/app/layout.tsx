"use client";
import {
  DesktopOutlined,
  FileOutlined,
  PieChartOutlined,
  TeamOutlined,
  UserOutlined,
} from "@ant-design/icons";
import { AntdRegistry } from "@ant-design/nextjs-registry";
import type { MenuProps } from "antd";
import { Breadcrumb, Layout, Menu, theme } from "antd";
import { useRouter, usePathname } from "next/navigation";
import React, { use, useEffect, useState } from "react";

const { Header, Content, Footer, Sider } = Layout;

type MenuItem = Required<MenuProps>["items"][number];

function getItem(
  label: React.ReactNode,
  key: React.Key,
  icon?: React.ReactNode,
  children?: MenuItem[]
): MenuItem {
  return {
    key,
    icon,
    children,
    label,
  } as MenuItem;
}

const routes = [
  {
    path: "/",
    label: "首页",
    icon: <PieChartOutlined />,
  },
  {
    path: "/measure",
    label: "检测",
    icon: <DesktopOutlined />,
  },
  {
    path: "/data",
    label: "数据",
    icon: <UserOutlined />,
    children: [
      {
        path: "/history",
        label: "历史记录",
      },
      {
        path: "/pending",
        label: "待处理",
      },
      {
        path: "/latest",
        label: "最新记录",
      },
    ],
  },
  {
    path: "/manage",
    label: "用户",
    icon: <TeamOutlined />,
    children: [
      {
        path: "/user",
        label: "用户管理",
      },
      {
        path: "/new",
        label: "注册审批",
      },
    ],
  },
  {
    path: "/file",
    label: "文件",
    icon: <FileOutlined />,
  },
];

const items: MenuItem[] = [
  getItem("首页", "/", <PieChartOutlined />),
  getItem("检测", "measure", <DesktopOutlined />),
  getItem("数据", "data", <UserOutlined />, [
    getItem("历史记录", "history"),
    getItem("待处理", "pending"),
    getItem("最新记录", "latest"),
  ]),
  getItem("用户", "manage", <TeamOutlined />, [
    getItem("用户管理", "user"),
    getItem("注册审批", "new"),
  ]),
  getItem("文件", "file", <FileOutlined />),
];

const RootLayout = ({ children }: React.PropsWithChildren) => {
  const router = useRouter();
  const pathname = usePathname();
  const paths = pathname.split("/").filter(Boolean);
  const [selectDefault, setSelectDefault] = useState<string[]>([]);
  const [openKeys, setOpenKeys] = useState<string[]>([]);
  const [collapsed, setCollapsed] = useState(false);
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  useEffect(() => {
    const path = pathname.split("/").filter(Boolean);
    console.log(path);
    if (path.length === 0) {
      setSelectDefault(["/"]);
    } else if (path.length === 1) {
      setSelectDefault([path[0]]);
    } else {
      setOpenKeys([path[0]]);
      setSelectDefault([path[1]]);
    }
  }, [pathname, setSelectDefault, setOpenKeys]);

  const goPath = (path: string[]) => {
    path.reverse();
    router.push(`/${path.join("/")}`);
  };

  return (
    <html lang="en">
      <body>
        <AntdRegistry>
          <Layout style={{ height: "100vh" }}>
            <Sider
              collapsible
              collapsed={collapsed}
              onCollapse={(value) => setCollapsed(value)}
              style={{ height: "100vh" }}
              defaultChecked={false}
            >
              <div />
              <Menu
                theme="dark"
                defaultOpenKeys={openKeys}
                defaultSelectedKeys={selectDefault}
                mode="inline"
                items={items}
                onSelect={({ keyPath }) => goPath(keyPath)}
                subMenuCloseDelay={1}
              />
            </Sider>
            <Layout>
              <Header style={{ padding: 0, background: colorBgContainer }} />
              <Content style={{ margin: "0 16px" }}>
                <Breadcrumb style={{ margin: "16px 0" }}>
                  {paths.map((path, index) => (
                    // 从 items 中找到 path 对应的 label
                    <Breadcrumb.Item key={index}>{path}</Breadcrumb.Item>
                  ))}
                  {/* <Breadcrumb.Item>User</Breadcrumb.Item>
                  <Breadcrumb.Item>Bill</Breadcrumb.Item> */}
                </Breadcrumb>
                <div
                  style={{
                    padding: 24,
                    height: "100%",
                    background: colorBgContainer,
                    borderRadius: borderRadiusLG,
                  }}
                >
                  {children}
                </div>
              </Content>
            </Layout>
          </Layout>
        </AntdRegistry>
      </body>
    </html>
  );
};

export default RootLayout;

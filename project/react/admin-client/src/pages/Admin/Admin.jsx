import React, { Suspense, useEffect } from "react";
import { useNavigate, Navigate, Outlet } from "react-router-dom";
import memoryUtils from "../../utils/memoryUtils";

import { Layout } from "antd";
import LeftNav from "../../components/LeftNav/LeftNav";
import Header from "../../components/Header/Header";
import storageUtils from "../../utils/storageUtils";
const { Footer, Sider, Content } = Layout;

export default function Admin() {
  const navigator = useNavigate();
  const user = memoryUtils.user; // 从内存中读取user

  /* ------ 如果用户未登录, 自动跳转到登录界面 ------ */
  useEffect(() => {
    if (!user || !user._id) {
      navigator("/login", { replace: true });
    }
  }, []);

  return (
    <Layout style={{ height: "100%" }}>
      <Sider>
        <LeftNav />
      </Sider>
      <Layout>
        <Header>Header</Header>
        <Content style={{ backgroundColor: "#fff", margin: "20px" }}>
          <Suspense fallback={<div>Loading...</div>}>
            <Outlet />
          </Suspense>
        </Content>
        <Footer style={{ textAlign: "center", color: "#A0A0A1" }}>
          推荐使用谷歌浏览器, 可以获得更好的体验
          <button
            onClick={() => {
              memoryUtils.user = {};
              storageUtils.removeUser();
              navigator("/login");
            }}
          >
            退出
          </button>
        </Footer>
      </Layout>
    </Layout>
  );
}

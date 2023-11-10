import React, { Suspense, useEffect } from "react";
import { useNavigate, Outlet } from "react-router-dom";
import memoryUtils from "../../utils/memoryUtils";

import { Layout } from "antd";
import LeftNav from "../../components/LeftNav/LeftNav";
import Header from "../../components/Header/Header";
const { Footer, Sider, Content } = Layout;

export default function Admin() {
  const navigator = useNavigate();
  const user = memoryUtils.user; // 从内存中读取user

  /* ------ 如果用户未登录, 自动跳转到登录界面 ------ */
  useEffect(() => {
    if (!user || !user._id) {
      navigator("/login", { replace: true });
    }
  }, [navigator, user]);

  return (
    <Layout style={{ minHeight: "100%" }}>
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
        </Footer>
      </Layout>
    </Layout>
  );
}

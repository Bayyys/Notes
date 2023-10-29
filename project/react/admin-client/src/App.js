import React from "react";
import { useRoutes } from "react-router-dom";
import routes from "./routes";
import { ConfigProvider } from "antd";

export default function App() {
  const element = useRoutes(routes);

  return (
    <ConfigProvider
      theme={{
        token: {
          colorPrimary: "#1DA57A",
        },
      }}
    >
      {element}
    </ConfigProvider>
  );
}

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 3000, // 指定默认端口
    open: "/", // 设置服务器启动时自动打开浏览器
    proxy: {  // 配置proxy
      "/api": {
        target: "http://localhost:5000",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
  plugins: [
    react({
      babel: {
        plugins: ["@babel/plugin-transform-react-jsx"], // jsx语法
      },
    }),
  ],
});

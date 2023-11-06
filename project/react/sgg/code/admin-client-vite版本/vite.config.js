import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import requireTransform from "vite-plugin-require-transform";
import commonjs from "@rollup/plugin-commonjs";
// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      "@ant-design/icons/lib/dist$": "@ant-design/icons/lib/dist/index.js",
    },
  },
  server: {
    port: 3000, // 指定默认端口
    open: "/", // 设置服务器启动时自动打开浏览器
    proxy: {
      // 配置proxy
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
    requireTransform({
      fileRegex: /.js$/,
    }),
    commonjs({
      include: /node_modules/,
      transformMixedEsModules: true,
    }),
  ],
});

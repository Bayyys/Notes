import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    open: true, // 自动打开浏览器
    port: 3000, // 启动端口号
    strictPort: false, // 如果端口号被占用，是否自动提升
  },
});

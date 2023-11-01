import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 3000,
    open: "/",
  },
  plugins: [react()],
  esbuild: { loader: { ".js": "jsx" } }, // <--- Added this line
});

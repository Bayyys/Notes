const path = require("path");
module.exports = {
  // 入口
  entry: "./src/main.js",
  // 输出
  output: {
    // path: 文件输出目录, 必须是绝对路径 (path.resolve(__dirname, 'dist'))
    // filename: 输出文件名 (main.js)
    path: path.resolve(__dirname, "dist"),
    filename: "main.js",
  },
  // 加载器
  module: {
    rules: [
      {
        // loader 配置
        test: /\.css$/, // 匹配文件
        use: ["style-loader", "css-loader"], // 使用 loader
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
    ],
  },
  // 插件
  plugins: [
    // plugin 配置
  ],
  // 模式
  mode: "development",
};

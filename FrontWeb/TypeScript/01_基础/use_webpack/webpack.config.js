const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

const isProduction = process.env.NODE_ENV === "production";

module.exports = {
  entry: "./src/index.ts",
  output: {
    path: isProduction ? path.resolve(__dirname, "dist") : undefined,
    filename: "bundle.js",
    environment: {
      arrowFunction: false, // 关闭webpack的箭头函数
    },
    clean: true, // 清理dist目录
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: ["babel-loader", "ts-loader"],
        exclude: /node_modules/,
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      // 生成html文件
      title: "TS测试", // html文件的title
    }),
  ],
  optimization: {
    minimize: false,
  },
  devtool: "inline-source-map", // 错误追踪
  resolve: {
    extensions: [".ts", ".js"], // 引入文件时，可以省略后缀名
  },
  devServer: {
    open: true,
    host: "localhost",
    port: 3000,
    hot: true,
    historyApiFallback: true,
  },
  mode: isProduction ? "production" : "development",
};

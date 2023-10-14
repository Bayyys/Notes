const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

const isProduction = process.env.NODE_ENV === "production";

const getStyleLoaders = (preProcessor) => {
  return [
    isProduction ? MiniCssExtractPlugin.loader : "style-loader",
    "css-loader",
    {
      loader: "postcss-loader",
      options: {
        postcssOptions: {
          plugins: [
            "postcss-preset-env", // 能解决大多数样式兼容性问题
          ],
        },
      },
    },
    preProcessor,
  ].filter(Boolean); // 不传参数, 默认为 undefined, filter(Booleran) 会过滤掉该项
};

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
        test: /\.less$/,
        use: getStyleLoaders("less-loader"),
      },
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
      template: "./public/index.html",
    }),
    isProduction &&
      new MiniCssExtractPlugin({
        filename: "static/css/[name].css",
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

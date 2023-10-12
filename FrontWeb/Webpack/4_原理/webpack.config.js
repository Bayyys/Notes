const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const BannerWebpackPlugin = require("./plugins/banner-webpack-plugin");
const CleanWebpackPlugin = require("./plugins/clean-webpack-plugin");
const AnalyzeWebpackPlugin = require("./plugins/analyze-webpack-plugin");
const InlineChunkWebpackPlugin = require("./plugins/inline-chunk-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "./dist"),
    filename: "js/[name].js",
    // clean: true,
  },
  module: {
    rules: [
      // {
      //   test: /\.js$/,
      //   loader: "./loaders/banner-loader",
      //   options: {
      //     author: "bayyy",
      //   },
      // },
      {
        test: /\.js$/,
        loader: "./loaders/babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
      {
        test: /\.(png|jpe?g|gif)$/,
        loader: "./loaders/file-loader",
        type: "javascript/auto", // 解决图片重复打包问题
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "public/index.html"),
    }),
    new BannerWebpackPlugin({
      author: "bayyy",
    }),
    new CleanWebpackPlugin(),
    new AnalyzeWebpackPlugin(),
    new InlineChunkWebpackPlugin([/runtime(.*)\.js$/g]),
  ],
  optimization: {
    splitChunks: {
      chunks: "all",
    },
    runtimeChunk: {
      name: (entrypoint) => `runtime~${entrypoint.name}`,
    },
  },
  mode: "production",
};

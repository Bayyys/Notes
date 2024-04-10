const path = require("path");
const ESLintWebpackPlugin = require("eslint-webpack-plugin");
const ReactRefreshWebpackPlugin = require("@pmmmwh/react-refresh-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerWebpackPlugin = require("css-minimizer-webpack-plugin");
const TerserWebpackPlugin = require("terser-webpack-plugin");
const CopyPlugin = require("copy-webpack-plugin");

const isProduction = process.env.NODE_ENV === "production";

// 获取处理样式的Loaders
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
  entry: "./src/main.js",
  output: {
    path: isProduction ? path.resolve(__dirname, "../dist") : undefined,
    filename: isProduction
      ? "static/js/[name].[contenthash:10].js"
      : "static/js/[name].js",
    chunkFilename: isProduction
      ? "static/js/[name].[contenthash:10].chunk.js"
      : "static/js/[name].chunk.js",
    assetModuleFilename: "static/media/[hash:10][ext][query]",
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: getStyleLoaders(),
      },
      {
        test: /\.less$/,
        use: getStyleLoaders("less-loader"),
      },
      {
        test: /\.s[ac]ss$/,
        use: getStyleLoaders("sass-loader"),
      },
      {
        test: /\.styl$/,
        use: getStyleLoaders("stylus-loader"),
      },
      // 处理图片
      {
        test: /\.(png|jpe?g|gif|webp|svg)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024, // 小于10kb的图片会被base64处理
          },
        },
      },
      // 处理字体
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
      },
      // 处理 js
      {
        test: /\.jsx?$/,
        exclude: /node_modules/, // 排除node_modules代码不编译
        loader: "babel-loader",
        options: {
          cacheDirectory: true, // 开启babel缓存
          cacheCompression: false, // 关闭babel缓存压缩
          plugins: [
            !isProduction && "react-refresh/babel", // js HMR
          ].filter(Boolean),
        },
      },
    ],
  },
  plugins: [
    new ESLintWebpackPlugin({
      context: path.resolve(__dirname, "../src"),
      exclude: "node_modules",
      cache: true,
      cacheLocation: path.resolve(
        __dirname,
        "../node_modules/.cache/.eslintcache"
      ),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "../public/index.html"),
    }),
    isProduction &&
      new MiniCssExtractPlugin({
        filename: "static/css/[name].[contenthash:10].css",
        chunkFilename: "static/css/[name].[contenthash:10].chunk.css",
      }),
    isProduction &&
      new CopyPlugin({
        patterns: [
          {
            from: path.resolve(__dirname, "../public"),
            to: path.resolve(__dirname, "../dist"),
            globOptions: {
              ignore: ["**/index.html"],
            },
          },
        ],
      }),
    !isProduction && new ReactRefreshWebpackPlugin(),
  ].filter(Boolean),
  optimization: {
    splitChunks: {
      chunks: "all",
    },
    runtimeChunk: {
      name: (entrypoint) => `runtime~${entrypoint.name}`,
    },
    minimize: isProduction,
    minimizer: [new CssMinimizerWebpackPlugin(), new TerserWebpackPlugin()],
  },
  resolve: {
    extensions: [".jsx", ".js", ".json"], // 自动补全文件扩展名，让jsx可以使用
  },
  mode: isProduction ? "production" : "development",
  devtool: isProduction ? "source-map" : "cheap-module-source-map",
  devServer: {
    open: true,
    host: "localhost",
    port: 3000,
    hot: true,
    historyApiFallback: true, // 解决react-router刷新404问题
  },
};

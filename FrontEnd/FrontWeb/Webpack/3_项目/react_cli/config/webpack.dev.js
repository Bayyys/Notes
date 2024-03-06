const path = require("path");
const ESLintWebpackPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const ReactRefreshWebpackPlugin = require("@pmmmwh/react-refresh-webpack-plugin");

const isDevelopment = process.env.NODE_ENV !== "production";

// 获取处理样式的Loaders
const getStyleLoaders = (preProcessor) => {
  return [
    "style-loader",
    "css-loader",
    {
      // 处理 css 兼容性问题
      // 配合 package.json 中 browserslist 来指定兼容性范围
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
    path: undefined,
    filename: "static/js/[name].js",
    chunkFilename: "static/js/[name].chunk.js",
    assetModuleFilename: "static/media/[hash:10][ext][query]",
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
          plugins: ["react-refresh/babel"], // js HMR
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
    new ReactRefreshWebpackPlugin(),
  ],
  optimization: {
    splitChunks: {
      chunks: "all",
    },
    runtimeChunk: {
      name: (entrypoint) => `runtime~${entrypoint.name}`,
    },
  },
  resolve: {
    extensions: [".jsx", ".js", ".json"], // 自动补全文件扩展名，让jsx可以使用
  },
  devServer: {
    open: true,
    host: "localhost",
    port: 3000,
    hot: true,
    historyApiFallback: true, // 解决react-router刷新404问题
  },
  mode: "development",
  devtool: "cheap-module-source-map",
};

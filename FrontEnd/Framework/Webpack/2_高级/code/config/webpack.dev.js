const os = require("os");
const path = require("path");
const ESLintWebpackPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

// cpu核数
const threads = os.cpus().length;

module.exports = {
  entry: "./src/main.js",
  output: {
    path: undefined, // 开发模式没有输出
    filename: "static/js/[name].js", // 入口文件打包输出资源命名方式
    chunkFilename: "static/js/[name].chunk.js", // 动态导入输出资源命名方式
    assetModuleFilename: "static/media/[name].[hash][ext]", // 图片、字体等资源命名方式（注意用hash）
  },
  module: {
    rules: [
      {
        oneOf: [
          {
            test: /\.css$/, // 匹配 .css 文件
            use: ["style-loader", "css-loader"], // Loader顺序 从右到左
          },
          {
            test: /\.less$/,
            use: ["style-loader", "css-loader", "less-loader"],
          },
          {
            test: /\.s[ac]ss$/,
            use: ["style-loader", "css-loader", "sass-loader"],
          },
          {
            test: /\.styl$/,
            use: ["style-loader", "css-loader", "stylus-loader"],
          },
          {
            test: /\.(png|jpe?g|gif|webp)$/,
            type: "asset",
            parser: {
              dataUrlCondition: {
                maxSize: 10 * 1024, // 小于10kb的图片会被base64处理
              },
            },
            // generator: {
            //   // [name] 原来的名字
            //   // [ext] 原来的后缀
            //   // [hash:8] 8位hash值
            //   // [path] 原来的路径
            //   // [contenthash] 内容hash
            //   // [query] query参数
            //   filename: "static/imgs/[name]-[hash:8][ext][query]",
            // },
          },
          {
            test: /\.(ttf|woff2?)$/,
            type: "asset/resource",
            // generator: {
            //   filename: "static/media/[hash:8][ext][query]",
            // },
          },
          {
            test: /\.js$/,
            exclude: /node_modules/, // 排除node_modules代码不编译
            // include: path.resolve(__dirname, "../src"), // 指定检查的目录
            use: [
              {
                loader: "thread-loader", // 开启多进程打包
                options: {
                  workers: threads, // 进程数
                },
              },
              {
                loader: "babel-loader",
                options: {
                  cacheDirectory: true, // 开启babel缓存
                  cacheCompression: false, // 关闭babel缓存压缩
                  plugins: ["@babel/plugin-transform-runtime"], // 减少代码体积
                },
              },
            ],
          },
        ],
      },
    ],
  },
  plugins: [
    new ESLintWebpackPlugin({
      // 指定需要检查文件的根目录
      context: path.resolve(__dirname, "../src"),
      exclude: "node_modules", // 排除node_modules目录
      cache: true, // 开启缓存
      // 缓存目录
      cacheLocation: path.resolve(
        __dirname,
        "../node_modules/.cache/.eslintcache"
      ),
      threads,
    }),
    new HtmlWebpackPlugin({
      // 以 public/index.html 为模板创建文件
      template: path.resolve(__dirname, "../public/index.html"),
    }),
  ],
  optimization: {},
  devServer: {
    host: "localhost", // 启动服务器域名
    port: "3000", // 启动服务器端口号
    open: true, // 是否自动打开浏览器
    hot: true, // 开启热更新
  },
  // 模式
  mode: "development",
  devtool: "cheap-module-source-map",
};

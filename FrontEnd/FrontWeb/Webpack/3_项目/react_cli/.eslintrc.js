module.exports = {
  extends: ["react-app"], // 继承 react 官方配置
  parserOptions: {
    babelOptions: {
      presets: [
        // 解决页面报错问题
        ["babel-preset-react-app", false], // 不使用默认配置
        "babel-preset-react-app/prod", // 使用生产环境配置
      ],
    },
  },
};

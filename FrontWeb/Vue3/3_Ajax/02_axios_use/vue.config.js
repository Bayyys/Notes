const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  // 方式一: 开启代理服务器
  // devServer: {
  //   proxy: 'http://localhost:5000'  // 改为后继服务器的地址
  // }

  // 方式二: 开启代理服务器(+ 代理前缀)
  devServer: {
    proxy: {
      // 代理前缀
      '5000': {
        target: 'http://localhost:5000',  // 改为后继服务器的地址
        pathRewrite: { '^/5000': '' }, // 代理前缀(会将前缀替换为空)
        // 即: http://localhost:5000/5000/xxx => http://localhost:5000/xxx
        // ws: true, // 支持websocket
        // changeOrigin: true // 支持跨域
      },
      '5001': {
        target: 'http://localhost:5001',
        pathRewrite: { '^/5001': '' }
      }
    }
  }
})

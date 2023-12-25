import vue from '@vitejs/plugin-vue'
import path from 'path'
import { createSvgIconsPlugin } from 'vite-plugin-svg-icons'
import { UserConfigExport, ConfigEnv } from 'vite'
import { viteMockServe } from 'vite-plugin-mock'
import vueSetupExtend from 'unplugin-vue-setup-extend-plus/vite'

export default ({ command }: ConfigEnv): UserConfigExport => {
  return {
    plugins: [
      createSvgIconsPlugin({
        // Specify the icon folder to be cached
        iconDirs: [path.resolve(process.cwd(), 'src/assets/icons')],
        // Specify symbolId format
        symbolId: 'icon-[dir]-[name]',
      }),
      vue(),
      vueSetupExtend({}),
      viteMockServe({
        localEnabled: command === 'serve', // 在开发环境下开启mock服务
      }),
    ],
    resolve: {
      alias: {
        // 设置别名
        '@': path.resolve(__dirname, './src'),
      },
    },
    server: {
      open: true, // 自动打开浏览器
      port: 3000, // 启动端口号
      strictPort: false, // 如果端口号被占用，是否自动提升
    },
    css: {
      preprocessorOptions: {
        scss: {
          javascriptEnabled: true,
          charset: false, // 关闭编译时 字符编码 报错问题
          // 引入全局变量
          additionalData: '@import "./src/styles/variable.scss";',
        },
      },
    },
  }
}

// 定义 用户相关 小仓库
import { defineStore } from 'pinia'
import { reqLogin, reqUserInfo, reqLogout } from '@/api/user_api'
import { GET_TOKEN, REMOVE_TOKEN, SET_TOKEN } from '@/utils/token'
import { UserState } from './types/type'
import type {
  LoginFormData,
  LoginResponseData,
  LogoutResponseData,
  UserInfoResponseData,
} from '@/api/user_api/type'
import { constantRoute } from '@/router/router'

// defineStore方法执行会返回一个 '函数', 函数作用就是让组件可以获取到仓库数据
// 第一个参数:小仓库名字  第二个参数:小仓库配置对象
const useUserStore = defineStore('User', {
  state: (): UserState => {
    return {
      token: GET_TOKEN(), // 用户token
      menuRoutes: constantRoute, // 菜单路由
      username: '', // 用户名
      avatar: '', // 用户头像
    }
  },
  // 异步 | 逻辑处理
  actions: {
    // 用户登录
    async userLogin(data: LoginFormData) {
      const res: LoginResponseData = await reqLogin(data) // 发送登录请求
      if (res.code === 200) {
        this.token = res.data as string // 将token存储到仓库中
        SET_TOKEN(res.data as string) // 将token存储到本地(防止刷新丢失, 且获取方便)
        return Promise.resolve('登录成功')
      } else {
        return Promise.reject(new Error(res.message))
      }
    },
    // 获取用户信息
    async userInfo() {
      const res: UserInfoResponseData = await reqUserInfo()
      if (res.code === 200) {
        this.username = res.data.name
        this.avatar = res.data.avatar
        return Promise.resolve('获取用户信息成功')
      } else {
        return Promise.reject(new Error(res.message))
      }
    },
    // 退出登录
    async userLogout() {
      const res: LogoutResponseData = await reqLogout()
      if (res.code === 200) {
        // 重置仓库数据
        this.token = ''
        this.username = ''
        this.avatar = ''
        // 删除本地token
        REMOVE_TOKEN()
        return Promise.resolve('退出登录成功')
      } else {
        return Promise.reject(new Error(res.message))
      }
    },
  },
  getters: {},
})
//对外暴露方法
export default useUserStore

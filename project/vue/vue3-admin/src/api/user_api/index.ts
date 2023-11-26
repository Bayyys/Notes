import request from '@/utils/request'
import type { LoginForm, LoginResponseData, UserInfoResponseData } from './type'

enum API {
  LOGIN_URL = '/user/login',
  USERINFO_URL = '/user/info',
}
// 用户登录 post {username, password}
export const reqLogin = (data: LoginForm) =>
  request.post<any, LoginResponseData>(API.LOGIN_URL, data)

// 获取用户信息 get
export const reqUserInfo = () =>
  request.get<any, UserInfoResponseData>(API.USERINFO_URL)

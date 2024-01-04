import request from '@/utils/request'
import type {
  LoginFormData,
  LoginResponseData,
  LogoutResponseData,
  UserInfoResponseData,
} from './type'

/* mock虚拟数据
// enum API {
//   LOGIN_URL = '/user/login',
//   USERINFO_URL = '/user/info',
// }
// // 用户登录 post {username, password}
// export const reqLogin = (data: LoginForm) =>
//   request.post<any, LoginResponseData>(API.LOGIN_URL, data)

// // 获取用户信息 get
// export const reqUserInfo = () =>
//   request.get<any, UserInfoResponseData>(API.USERINFO_URL)
*/

// 项目用户相关的请求地址
enum API {
  LOGIN_URL = '/admin/acl/index/login',
  USERINFO_URL = '/admin/acl/index/info',
  LOGOUT_URL = '/admin/acl/index/logout',
}

// 登录接口
export const reqLogin = (data: LoginFormData) =>
  request.post<any, LoginResponseData>(API.LOGIN_URL, data)
// 获取用户信息
export const reqUserInfo = () =>
  request.get<any, UserInfoResponseData>(API.USERINFO_URL)
// 退出登录
export const reqLogout = () =>
  request.post<any, LogoutResponseData>(API.LOGOUT_URL)

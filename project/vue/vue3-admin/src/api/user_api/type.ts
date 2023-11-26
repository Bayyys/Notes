/* --- 用户登录 --- */
// 用户登录接口参数类型
export interface LoginForm {
  username: string
  password: string
}

interface dataType {
  token: string
}

// 用户登录接口返回数据类型
export interface LoginResponseData {
  code: number
  data: dataType
}

/* --- 获取用户信息 --- */
interface userInfo {
  userId: number
  avatar: string
  username: string
  password: string
  desc: string
  roles: string[]
  buttons: string[]
  routes: string[]
  token: string
}

interface user {
  checkUser: userInfo
}
// 获取用户信息接口返回数据类型
export interface UserInfoResponseData {
  code: number
  data: user
}

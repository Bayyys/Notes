// 定义全部接口返回数据类型
export interface ResponseData {
  code: number
  message: string
  ok: boolean
}
/* --- 用户登录 --- */
// 用户登录接口参数类型
export interface LoginFormData {
  username: string
  password: string
}

// 登录接口返回数据类型
export interface LoginResponseData extends ResponseData {
  data: string
}

// 获取用户信息接口返回数据类型
export interface UserInfoResponseData extends ResponseData {
  data: {
    routes: string[]
    buttons: string[]
    roles: string[]
    name: string
    avatar: string
  }
}

// 退出登录接口返回数据类型
export interface LogoutResponseData extends ResponseData {
  data: null
}

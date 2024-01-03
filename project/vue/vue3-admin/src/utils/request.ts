import axios from 'axios' // 引入axios
import { ElMessage } from 'element-plus'
// 引入用户相关仓库
import useUserStore from '@/store/modules/user'

//创建axios实例
const request = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_API, // 基础路径
  timeout: 5000, // 请求超时时间
})

//请求拦截器
request.interceptors.request.use((config) => {
  // config配置对象, 例如: headers属性请求头, 可以给服务器端携带公共参数
  // config.headers.test = 123
  const userStore = useUserStore() // 获取用户相关仓库
  if (userStore.token) {
    // 如果token存在, 则给请求头添加token
    config.headers.token = userStore.token
  }
  return config
})

//响应拦截器
request.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    //处理网络错误
    let msg = '' // 提示信息
    const status = error.response.status // 状态码
    switch (status) {
      case 401:
        msg = 'token过期'
        break
      case 403:
        msg = '无权访问'
        break
      case 404:
        msg = '请求地址错误'
        break
      case 500:
        msg = '服务器出现问题'
        break
      default:
        msg = '无网络'
    }
    ElMessage({
      type: 'error',
      message: msg,
    })
    return Promise.reject(error)
  },
)

export default request

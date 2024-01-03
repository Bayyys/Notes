// 封装本地存储数据与读取数据的方法
// 存储TOKEN
export const SET_TOKEN = (token: string) => {
  localStorage.setItem('TOKEN', token)
}

// 获取TOKEN
export const GET_TOKEN = (): string => {
  return localStorage.getItem('TOKEN') || ''
}

// 删除TOKEN
export const REMOVE_TOKEN = () => {
  localStorage.removeItem('TOKEN')
}

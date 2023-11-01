/*
要求: 能根据接口文档定义接口请求
包含应用中所有接口请求函数的模块
每个函数的返回值都是promise

基本要求: 能根据接口文档定义接口请求函数
 */
import ajax from "./ajax";

const BASE = "/api";

// 登陆
export const reqLogin = (username, password) =>
  ajax(BASE + "/login", { username, password }, "POST");

// 添加用户
export const reqAddUser = (user) =>
  ajax(BASE + "/manage/user/add", user, "POST");

// 获取所有用户的列表
export const reqUsers = () => ajax(BASE + "/manage/user/list");

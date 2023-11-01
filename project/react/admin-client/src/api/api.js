/*
要求: 能根据接口文档定义接口请求
包含应用中所有接口请求函数的模块
每个函数的返回值都是promise

基本要求: 能根据接口文档定义接口请求函数
 */
import ajax from "./ajax";

/* ----- 百度地图 api ----- */
// jsonp请求的接口请求函数
export const getRegionCode = async (city) => {
  try {
    const res = await ajax(BASE + "/region", city, "GET");
    if (res.status === 0) {
      if (res.result_size === 0) {
        return "unknown_city";
      }
      return res.districts.code;
    } else {
      return "error";
    }
  } catch (error) {
    return "error";
  }
};

export const getWeather = async (city) => {
  const region_code = getRegionCode(city);
  if (region_code === "error") {
    return Promise.reject("定位错误");
  }
  if (region_code === "unknown_city") {
    return Promise.reject("未知城市");
  }
  try {
    const res = await ajax(BASE + "/weather", region_code, "GET");
    if (res.status === 0 && res.message === "success") {
      return Promise.resolve(res.result.now.text);
    } else {
      return Promise.reject("未知城市");
    }
  } catch (error) {
    return Promise.reject("未知城市");
  }
};

const BASE = "/api";

// 登陆
export const reqLogin = (username, password) =>
  ajax(BASE + "/login", { username, password }, "POST");

// 添加用户
export const reqAddUser = (user) =>
  ajax(BASE + "/manage/user/add", user, "POST");

// 获取所有用户的列表
export const reqUsers = () => ajax(BASE + "/manage/user/list");

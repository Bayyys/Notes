/**
 * 日期处理工具类
 */

export function formateDate(time) {
  if (!time) return "";
  let date = new Date(time);
  return `${date.getFullYear()}-${padLeftZero(
    date.getMonth() + 1
  )}-${padLeftZero(date.getDay())} ${padLeftZero(
    date.getHours()
  )}:${padLeftZero(date.getMinutes())}:${padLeftZero(date.getSeconds())}`;
}

function padLeftZero(num) {
  return num.toString().padStart(2, "0");
}

/* 时间相关处理 */

/**
 * @description: 获取当前时间段
 * @returns {string} [凌晨, 早上, 上午, 中午, 下午, 晚上]
 */
export const getTimePeriod = (): string => {
  let message = ''
  const hour = new Date().getHours()
  if (hour >= 0 && hour <= 6) {
    message = '凌晨'
  } else if (hour > 6 && hour <= 8) {
    message = '早上'
  } else if (hour > 8 && hour <= 11) {
    message = '上午'
  } else if (hour > 11 && hour <= 14) {
    message = '中午'
  } else if (hour > 14 && hour <= 18) {
    message = '下午'
  } else if (hour > 18 && hour <= 24) {
    message = '晚上'
  }
  return message
}

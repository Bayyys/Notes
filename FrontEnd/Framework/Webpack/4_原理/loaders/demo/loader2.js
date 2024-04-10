// // 方法一
// module.exports = function (content, map, meta) {
//   return content;
// };

// 方法二: 使用 this.callback() 方法
module.exports = function (content, map, meta) {
  console.log("loader2");
  // params1: err 代表错误信息，如果没有错误，传递 null
  // params2: content 代表转换后的内容
  // params3: map 代表 source-map, 继续传递 source-map
  // params4: meta 代表其他信息, 给下一个 loader 传递参数
  this.callback(null, content, map, meta);
  return; // 当调用 callback() 函数时，总是返回 undefined
};

// 同步loader
// module.exports = function (content) {
//   return content;
// };

module.exports = function (content, map, meta) {
  // console.log("test1");
  /*
    第一个参数：err 代表是否有错误
    第二个参数：content 处理后的内容
    第三个参数：source-map 继续传递source-map
    第四个参数：meta 给下一个loader传递参数
  */
  this.callback(null, content, map, meta);
  // 同步loader中不能进行异步操作
  // setTimeout(() => {
  //   console.log("test1");
  //   this.callback(null, content, map, meta);
  // }, 1000);
};

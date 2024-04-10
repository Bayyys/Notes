// 异步 loader
module.exports = function (content, map, meta) {
  const callback = this.async();
  // 进行异步操作
  setTimeout(() => {
    console.log("loader3");
    callback(null, content, map, meta);
  }, 1000);
};
// raw loader 接收到的 content 是一个 Buffer 数据
module.exports = function (content) {
  // content是一个Buffer数据
  console.log(content);
  console.log("loader4");
  return content;
};
module.exports.raw = true; // 开启 Raw Loader

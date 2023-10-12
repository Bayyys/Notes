const loaderUtils = require("loader-utils");

module.exports = function (content) {
  // 1. 根据文件内容生产一个新的文件名称
  let filename = loaderUtils.interpolateName(this, "[hash].[ext][query]", {
    content,
  });
  // 输出文件
  filename = `images/${filename}`;
  this.emitFile(filename, content);
  // 暴露出去，给js引用。
  // 记得加上''
  // 返回：module.exports = "文件路径（文件名）
  return `module.exports = "${filename}"`;
};

// loader 解决的是二进制的内容
// 图片是 Buffer 数据
module.exports.raw = true;

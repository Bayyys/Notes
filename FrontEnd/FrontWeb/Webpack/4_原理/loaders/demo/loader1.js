/*
  loader 就是一个函数
  当 webpack 解析资源时, 会调用相应的 loader 对资源进行转换
  接收参数
    content 资源文件内容
    map     资源文件 sourcemap
    meta    其他元信息 (其他loader传递过来的信息)
 */
module.exports = function (content) {
  console.log(content);
  return content;
};

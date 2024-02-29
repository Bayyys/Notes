// JSON.parse() hook -> 用于将一个JSON字符串转换为对象
!(function () {
  var parse_ = JSON.parse;
  JSON.parse = function (arg) {
    console.log("Crawled JSON.parse: " + arg);
    debugger;
    return parse_(arg);
  };
})();

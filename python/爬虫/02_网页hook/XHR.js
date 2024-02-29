// XHR(xhr 请求的参数)
(function () {
  var open = window.XMLHttpRequest.prototype.open;
  window.XMLHttpRequest.prototype.open = function (method, url, async) {
    if (url.indexOf("参数名称") != -1) {
      // 例如要查找 v=xxx 的参数
      // if (url.indexOf("v=") != -1) {...}
      console.log("Crawled XHR: " + url);
      debugger;
    }
    return open.apply(this, arguments);
  };
})();

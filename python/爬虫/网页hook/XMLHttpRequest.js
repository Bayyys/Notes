// XMLHttpRequest (header 参数)

(function () {
  var sh = window.XMLHttpRequest.prototype.setRequestHeader;
  window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
    if (key == "header 的参数 key") {
      console.log("Crawled XMLHttpRequest Header: " + key + " = " + value);
      debugger;
    }
    return sh.apply(this, arguments);
  };
})();

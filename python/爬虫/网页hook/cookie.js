// cookie

(function () {
  var cookieTemp = "";
  Object.defineProperty(document, "cookie", {
    set: function (val) {
      if (val.indexOf("v") != -1) {
        debugger;
      }
      console.log("Hook 捕获到 cookie 设置->", val);
      cookieTemp = val;
      return val;
    },
    get: function () {
      return cookieTemp;
    },
  });
})();

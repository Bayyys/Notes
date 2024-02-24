// 方法一
(function (/*args*/) {
  /* code */
  console.log("IIFE-1");
})();

// 方法二
(function (/*args*/) {
  /* code */
  console.log("IIFE-2");
})();

// 方法三 (可以使用包括 !, +, - 等在内的一元运算符)
!(function (/*args*/) {
  /* code */
  console.log("IIFE-3");
})();

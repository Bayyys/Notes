// 不同方式表示时间监听
window.addEventListener("load", function () {
  console.log("load");
});
window.onload = function () {
  console.log("onother load func");
};

// 防抖函数
const debounce = (fn, delay) => {
  let timer = null;
  return function () {
    clearTimeout(timer);
    timer = setTimeout(fn, delay);
  };
};

// 窗口尺寸改变的加载
window.onresize = debounce(() => {
  console.log("resize");
}, 500);

function raf() {
  requestAnimationFrame(() => {
    // 设置动画, 使得每次刷新都会执行
    // ...
    raf(); // 递归调用
  });
}

const btn = document.getElementById("btn");

btn?.addEventListener("click", function () {
  const list = document.getElementsByClassName("list")[0];
  console.log(list);
  const items = document.querySelectorAll(".item");
  console.log(items);
  for (let i = 0; i < items.length; i++) {
    const copy = items[i].cloneNode(true);
    list?.appendChild(copy);
  }
});

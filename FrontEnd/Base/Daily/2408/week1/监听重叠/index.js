const loading = document.querySelector(".loading");

// 创建一个观察者
const observer = new IntersectionObserver(
  (entries) => {
    if (entries[0].isIntersecting) {
      // 可以识别进入/离开视窗
      console.log("loading is intersecting");
    }
  }, // entries 是一个数组，包含所有被观察的元素
  {
    threshold: 0.5, // 交叉比例
  }
);

// 开始监听
observer.observe(loading); // 无第二个参数，表示监听整个视窗
// observer.observe(...)  // 可以监听多个元素

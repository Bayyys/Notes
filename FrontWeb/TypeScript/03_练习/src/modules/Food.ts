// 定义食物类
export default class Food {
  // 食物对应的元素
  element: HTMLElement;
  constructor() {
    this.element = document.getElementById("food")!;
  }

  // 获取食物的X轴坐标
  get X() {
    return this.element.offsetLeft;
  }

  get Y() {
    return this.element.offsetTop;
  }

  // 修改食物位置
  change() {
    // 生成随机位置
    // 食物的位置最小是0，最大是290
    // 蛇移动一次就是一格，一格的大小就是10，所以要求食物的坐标必须是整10
    const left = Math.round(Math.random() * 29) * 10;
    const top = Math.round(Math.random() * 29) * 10;

    this.element.style.left = left + "px";
    this.element.style.top = top + "px";
  }
}

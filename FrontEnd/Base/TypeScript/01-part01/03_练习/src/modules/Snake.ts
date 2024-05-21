export default class Snake {
  head: HTMLElement;
  element: HTMLElement;
  body: HTMLCollection;

  constructor() {
    this.head = document.querySelector("#snake > div") as HTMLElement;
    this.element = document.getElementById("snake")!;
    this.body = this.element.getElementsByTagName("div");
  }

  // 获取蛇的坐标（蛇头坐标）
  get X() {
    return this.head.offsetLeft;
  }

  get Y() {
    return this.head.offsetTop;
  }

  set X(value: number) {
    if (this.X === value) {
      return;
    }
    if (value < 0 || value > 290) {
      // 进入判断说明蛇撞墙了
      throw new Error("蛇撞墙了！");
    }

    if (this.body[1] && (this.body[1] as HTMLElement).offsetLeft === value) {
      // 如果发生了掉头，让蛇向反方向继续移动
      if (value > this.X) {
        // 如果新值value大于旧值X，则说明蛇在向右走，此时发生掉头，应该使蛇继续向左走
        value = this.X - 10;
      } else {
        value = this.X + 10;
      }
    }
    this.moveBody();
    this.head.style.left = value + "px";
    this.checkHeadBody();
  }

  set Y(value: number) {
    if (this.Y === value) {
      return;
    }
    if (value < 0 || value > 290) {
      throw new Error("蛇撞墙了！");
    }
    if (this.body[1] && (this.body[1] as HTMLElement).offsetTop === value) {
      // 如果发生了掉头，让蛇向反方向继续移动
      if (value > this.Y) {
        value = this.Y - 10;
      } else {
        value = this.Y + 10;
      }
    }
    this.moveBody();
    this.head.style.top = value + "px";
    this.checkHeadBody();
  }

  // 蛇增加身体的方法
  addBody() {
    // 向element中添加一个div
    this.element.insertAdjacentHTML("beforeend", "<div></div>");
  }

  moveBody() {
    // 将后边的身体设置为前边身体的位置
    // 遍历获取所有的身体
    for (let i = this.body.length - 1; i > 0; i--) {
      // 获取前边身体的位置
      let X = (this.body[i - 1] as HTMLElement).offsetLeft;
      let Y = (this.body[i - 1] as HTMLElement).offsetTop;

      // 将值设置到当前身体上
      (this.body[i] as HTMLElement).style.left = X + "px";
      (this.body[i] as HTMLElement).style.top = Y + "px";
    }
  }

  checkHeadBody() {
    // 获取所有的身体，检查其是否和蛇头的坐标发生重叠
    for (let i = 1; i < this.body.length; i++) {
      let bd = this.body[i] as HTMLElement;
      if (this.X === bd.offsetLeft && this.Y === bd.offsetTop) {
        throw new Error("撞到自己了！");
      }
    }
  }
}

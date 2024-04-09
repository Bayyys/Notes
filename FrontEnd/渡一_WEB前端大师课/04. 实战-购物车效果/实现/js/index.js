/**
 * 单个商品
 */
class UIGoods {
  constructor(g) {
    this.data = g;
    this.choose = 0;
  }
  // 商品总价
  getTotalPrice() {
    return this.data.price * this.choose;
  }
  // 商品是否选中
  isChoose() {
    return this.choose > 0;
  }
  // 修改数量
  increase() {
    this.choose++;
  }
  decrease() {
    if (this.choose > 0) {
      this.choose--;
    }
  }
}

/**
 * 商品列表
 */
class UIData {
  constructor() {
    var uiGoods = [];
    for (var i = 0; i < goods.length; i++) {
      uiGoods.push(new UIGoods(goods[i]));
    }
    this.uiGoods = uiGoods; // 商品列表
    this.deliveryThreshold = 30; // 配送门槛
    this.deliveryPrice = 5; // 配送费
  }
  // 总价
  getTotalPrice() {
    var totalPrice = 0;
    for (var i = 0; i < this.uiGoods.length; i++) {
      totalPrice += this.uiGoods[i].getTotalPrice();
    }
    return totalPrice;
  }
  // 商品总数
  getTotalCount() {
    var totalCount = 0;
    for (var i = 0; i < this.uiGoods.length; i++) {
      totalCount += this.uiGoods[i].choose;
    }
    return totalCount;
  }
  // 是否有选中商品
  hasGoodsInCar() {
    return this.getTotalCount() > 0;
  }
  // 是否满足配送门槛
  isCrossDeliveryThreshold() {
    return this.getTotalPrice() >= this.deliveryThreshold;
  }
  // 增加某件商品
  increase(index) {
    this.uiGoods[index].increase();
  }
  // 减少某件商品
  decrease(index) {
    this.uiGoods[index].decrease();
  }

  // 判断商品 是否选中
  isChoose(index) {
    return this.uiGoods[index].isChoose();
  }
}

// 整个界面
class UI {
  constructor() {
    this.uiData = new UIData(); // 数据
    this.doms = {
      goodsContainer: document.querySelector(".goods-list"), // 商品列表
      deliveryPrice: document.querySelector(".footer-car-tip"), // 配送费
      footerPay: document.querySelector(".footer-pay"), // 起送区域
      footerPayInnerSpan: document.querySelector(".footer-pay span"), // 配送费差额
      totalPrice: document.querySelector(".footer-car-total"), // 总价
      car: document.querySelector(".footer-car"), // 购物车图标
      badge: document.querySelector(".footer-car-badge"), // 商品数量
    };
    this.createHTML(); // 创建商品列表
    this.updateFooter(); // 更新底部
    this.animateListener(); // 动画监听
    var carRect = this.doms.car.getBoundingClientRect();
    var jumpTarget = {
      x: carRect.left + carRect.width / 2,
      y: carRect.top + carRect.height / 5,
    };
    this.jumpTarget = jumpTarget;
  }

  // 根据商品数据创建商品列表的元素
  createHTML() {
    var html = "";
    for (var i = 0; i < this.uiData.uiGoods.length; i++) {
      var g = this.uiData.uiGoods[i];
      html += `
      <div class="goods-item">
        <img src="${g.data.pic}" alt="" class="goods-pic">
        <div class="goods-info">
          <h2 class="goods-title">${g.data.title}</h2>
          <p class="goods-desc">${g.data.desc}</p>
          <p class="goods-sell">
            <span>月售 ${g.data.sellNumber}</span>
            <span>好评率${g.data.favorRate}%</span>
          </p>
          <div class="goods-confirm">
            <p class="goods-price">
              <span class="goods-price-unit">￥</span>
              <span>${g.data.price}</span>
            </p>
            <div class="goods-btns">
              <i index="${i}" class="iconfont i-jianhao"></i>
              <span>${g.choose}</span>
              <i index="${i}" class="iconfont i-jiajianzujianjiahao"></i>
            </div>
          </div>
        </div>
      </div>`;
    }
    this.doms.goodsContainer.innerHTML = html;
  }

  // 商品数量变化
  increase(index) {
    this.uiData.increase(index);
    this.updateGoodsItem(index);
    this.updateFooter();
  }

  decrease(index) {
    this.uiData.decrease(index);
    this.updateGoodsItem(index);
    this.updateFooter();
  }

  // 更新商品元素显示状态
  updateGoodsItem(index) {
    var goodsDom = this.doms.goodsContainer.children[index];
    if (this.uiData.isChoose(index)) {
      goodsDom.classList.add("active");
    } else {
      goodsDom.classList.remove("active");
    }
    goodsDom.querySelector(".goods-btns span").textContent =
      this.uiData.uiGoods[index].choose;
  }

  // 更新底部
  updateFooter() {
    this.updateDeliveryPrice();
    this.updateTotalPrice();
  }

  // 更新总价
  updateTotalPrice() {
    // 设置配送费
    this.doms.deliveryPrice.textContent = `配送费￥${this.uiData.deliveryPrice}`;
    // 总价
    var total = this.uiData.getTotalPrice();
    this.doms.totalPrice.textContent = total.toFixed(2);
    if (this.uiData.hasGoodsInCar()) {
      this.doms.car.classList.add("active");
      this.doms.badge.textContent = this.uiData.getTotalCount();
    } else {
      this.doms.car.classList.remove("active");
      this.doms.badge.textContent = "";
    }
  }

  // 更新配送费部分
  updateDeliveryPrice() {
    // 更新起送限制
    if (this.uiData.isCrossDeliveryThreshold()) {
      this.doms.footerPay.classList.add("active");
    } else {
      this.doms.footerPay.classList.remove("active");
      // 更新还差多少钱
      var dis = this.uiData.deliveryThreshold - this.uiData.getTotalPrice();
      dis = Math.round(dis);
      this.doms.footerPayInnerSpan.textContent = `还差￥${dis}元起送`;
    }
  }

  // 动画监听事件
  animateListener() {
    this.doms.car.addEventListener("animationend", () => {
      this.doms.car.classList.remove("animate");
    });
  }

  // 动画实现: 购物车动画
  carAnimate() {
    this.doms.car.classList.add("animate");
  }

  // 动画实现: 商品 +1 跳跃抛物线
  goodItemJump(index) {
    // 找到对应商品的加号
    var btnAdd = this.doms.goodsContainer.children[index].querySelector(
      ".i-jiajianzujianjiahao"
    );
    var rect = btnAdd.getBoundingClientRect();
    var start = {
      x: rect.left,
      y: rect.top,
    };
    // 跳吧
    var div = document.createElement("div");
    div.className = "add-to-car";
    var i = document.createElement("i");
    i.className = "iconfont i-jiajianzujianjiahao";
    // 设置初始位置
    div.style.transform = `translateX(${start.x}px)`;
    i.style.transform = `translateY(${start.y}px)`;
    div.appendChild(i);
    document.body.appendChild(div);
    // 强行渲染
    div.clientWidth;

    // 设置结束位置
    div.style.transform = `translateX(${this.jumpTarget.x}px)`;
    i.style.transform = `translateY(${this.jumpTarget.y}px)`;
    div.addEventListener(
      "transitionend",
      () => {
        div.remove();
        this.carAnimate();
      },
      {
        once: true, // 事件仅触发一次
      }
    );
  }
}

var ui = new UI();

// 点击商品 +1
ui.doms.goodsContainer.addEventListener("click", (e) => {
  var target = e.target;
  if (target.classList.contains("i-jiajianzujianjiahao")) {
    var index = target.getAttribute("index");
    ui.goodItemJump(index);
    ui.increase(index);
  }
  if (target.classList.contains("i-jianhao")) {
    var index = target.getAttribute("index");
    ui.decrease(index);
  }
});

window.addEventListener("keypress", function (e) {
  if (e.code === "Equal") {
    ui.increase(0);
  } else if (e.code === "Minus") {
    ui.decrease(0);
  }
});

// 完整的自定义hook
// 定义数据+定义监听函数+监听事件

import { reactive, onMounted, onBeforeUnmount } from "vue";
export default function () {
  // 1. 创建响应式对象
  const points = reactive({
    x: 0,
    y: 0,
  });

  // 2. 创建监听函数
  function showPoints(e) {
    points.x = e.pageX;
    points.y = e.pageY;
    console.log(points.x, points.y);
  }

  // 3. 监听事件
  onMounted(() => {
    window.addEventListener("click", showPoints);
  });

  onBeforeUnmount(() => {
    window.removeEventListener("click", showPoints);
  });

  return points;
}

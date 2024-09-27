---
title: 2024-09-week1 每日汇总
tags: ['CSS']
---

## 文字连续光影变换

> `CSS`

```html
  <div class="container">
    <span>B</span>
    <span>A</span>
    <span>Y</span>
    <span>Y</span>
    <span>Y</span>
    <span>S</span>
  </div>
```

```less
span {
  color: #faebd7;
  font-size: 40vh;
  align-content: center;
  animation: word-shadowing 1s ease-in-out infinite alternate;
}

@keyframes word-shadowing {
  to {
    color: #ff0266;
    text-shadow: 20px 0 70px #ff0266;
  }
}

each(range(10), {
  span:nth-child(@{value}) {
    animation-delay: 0.2s * @value;
  }
})
```


import React from "react";
import { useSearchParams, useLocation } from "react-router-dom";

export default function Detail() {
  // 数组的解构赋值
  const [searchParams, setSearchParams] = useSearchParams();
  // 需要调用 get() 方法获取对应的参数值
  const id = searchParams.get("id");
  const title = searchParams.get("title");
  const content = searchParams.get("content");
  const location = useLocation();
  console.log(location);
  return (
    <div>
      <ul>
        <li>消息编号: {id}</li>
        <li>消息标题: {title}</li>
        <li>消息内容: {content}</li>
      </ul>
      <button
        onClick={() => {
          setSearchParams("id=008&title=新数据&content=新内容");
        }}
      >
        更新接收到的数据
      </button>
    </div>
  );
}

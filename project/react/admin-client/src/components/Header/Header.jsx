import React, { Suspense, useEffect, useState } from "react";
import "./Header.less";
import { getWeather } from "../../api/api";

export default function Header() {
  const [weather, setWeather] = useState("");
  // 在界面渲染完成后，发送请求获取天气信息
  useEffect(() => {
    getWeather().then((res) => {
      setWeather(res);
    });
  }, []);
  return (
    <div className="header">
      <div className="header-top">
        <span>欢迎, admin</span>
        <a href="#!" className="logout">
          退出
        </a>
      </div>
      <div className="header-bottom">
        <div className="header-bottom-left">首页</div>
        <div className="header-bottom-right">
          <span>2023-10-31 23:39:31</span>
          <img
            src="http://api.map.baidu.com/images/weather/day/qing.png"
            alt="wheather"
          />
          <span>{weather}</span>
        </div>
      </div>
    </div>
  );
}

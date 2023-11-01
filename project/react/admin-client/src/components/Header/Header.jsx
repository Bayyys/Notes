import React from "react";
import "./Header.less";

export default function Header() {
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
          <span>晴</span>
        </div>
      </div>
    </div>
  );
}

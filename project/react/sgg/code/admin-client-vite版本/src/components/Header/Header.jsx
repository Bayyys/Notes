import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Modal, Button } from "antd";
import { CompassOutlined } from "@ant-design/icons";
import { pinyin } from "pinyin-pro";
import "./Header.less";
import { getWeather } from "../../api/api";
import memoryUtils from "../../utils/memoryUtils";
import storageUtils from "../../utils/storageUtils";
import { getMunuName as getMenuName } from "../../utils/menuUtils";
import menuList from "../../config/menuConfig";
import Timer from "./Timer";

export default function Header() {
  const [weather, setWeather] = useState("");
  const [city, setCity] = useState("");
  const [modal, contextHolder] = Modal.useModal();

  const username = memoryUtils.user.username;
  const pathname = useLocation().pathname;
  const title = getMenuName(menuList, pathname);
  const navigate = useNavigate();

  const onLogout = () => {
    modal.confirm({
      content: "确定退出吗?",
      onOk: () => {
        // 删除保存的 user 数据, 跳转到 login
        memoryUtils.user = {};
        storageUtils.removeUser();
        navigate("/login", { replace: true });
      },
    });
  };

  // 在界面渲染完成后，发送请求获取天气信息
  useEffect(() => {
    getWeather().then((res) => {
      setWeather(res.weather);
      setCity(res.city);
    });
  }, []);

  return (
    <div className="header">
      <div className="header-top">
        <span>欢迎, {username}</span>
        <Button type="link" onClick={onLogout}>
          退出
        </Button>
      </div>
      <div className="header-bottom">
        <div className="header-bottom-left">{title}</div>
        <div className="header-bottom-right">
          <Timer />
          <span>
            <CompassOutlined />
            {city}
          </span>
          <img
            src={`http://api.map.baidu.com/images/weather/day/${pinyin(
              weather,
              { toneType: "none", type: "string" }
            ).replace(/\s*/g, "")}.png`}
            alt="wheather"
          />
          <span>{weather}</span>
        </div>
      </div>
      {contextHolder}
    </div>
  );
}

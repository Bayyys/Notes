import React from "react";
import { NavLink, Outlet } from "react-router-dom";

export default function Home() {
  return (
    <div>
      <h1>Home内容</h1>
      <div>
        <ul className="nav nav-tabs">
          <li>
            <NavLink className="list-group-item" to="news">
              News
            </NavLink>
          </li>
          <li>
            <NavLink className="list-group-item" to="message">
              Message
            </NavLink>
          </li>
        </ul>
        {/* 指定子路由规则 */}
        <Outlet />
      </div>
    </div>
  );
}

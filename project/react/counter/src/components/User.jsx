import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { setUsername, setPassword } from "../redux/user";

export default function User() {
  const user = useSelector((state) => state.user);
  const dispatch = useDispatch();
  return (
    <div id="app">
      <h1>用户界面</h1>
      <h2>当前用户为: {user.username}</h2>
      <div>
        用户名:{" "}
        <input
          value={user.username}
          onChange={(e) => dispatch(setUsername(e.target.value))}
        />
      </div>
      <div>
        密码:{" "}
        <input
          value={user.password}
          onChange={(e) => dispatch(setPassword(e.target.value))}
        />
      </div>
    </div>
  );
}

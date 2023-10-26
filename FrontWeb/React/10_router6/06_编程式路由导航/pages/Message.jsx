import React, { useState } from "react";
import { Link, Outlet, useNavigate } from "react-router-dom";

export default function Message() {
  const [message] = useState([
    { id: 1, title: "message001", content: "001" },
    { id: 2, title: "message003", content: "002" },
    { id: 3, title: "message005", content: "003" },
  ]);
  const navigate = useNavigate();
  function showDetail(m) {
    navigate("detail", {
      replace: false,
      state: {
        id: m.id,
        title: m.title,
        content: m.content,
      },
    });
  }
  return (
    <div>
      <ul>
        {message.map((m) => {
          return (
            <li key={m.id}>
              <Link
                to="detail"
                state={{ id: m.id, title: m.title, content: m.content }}
              >
                {m.title}
              </Link>
              <button
                onClick={() => {
                  showDetail(m);
                }}
              >
                查看详情
              </button>
              <button onClick={() => navigate(-1)}>后退</button>
              <button onClick={() => navigate(1)}>前进</button>
            </li>
          );
        })}
      </ul>
      <Outlet />
    </div>
  );
}

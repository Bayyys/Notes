import React, { useState } from "react";
import { Link, Outlet } from "react-router-dom";

export default function Message() {
  const [message] = useState([
    { id: 1, title: "message001", content: "001" },
    { id: 2, title: "message003", content: "002" },
    { id: 3, title: "message005", content: "003" },
  ]);
  return (
    <div>
      <ul>
        {message.map((m) => {
          return (
            <li key={m.id}>
              <Link
                to={`detail?id=${m.id}&title=${m.title}&content=${m.content}`}
              >
                {m.title}
              </Link>
            </li>
          );
        })}
      </ul>
      <Outlet />
    </div>
  );
}

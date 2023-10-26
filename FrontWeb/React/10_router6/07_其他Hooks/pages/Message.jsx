import React, { useState } from "react";
import { Link, Outlet } from "react-router-dom";
import {
  useInRouterContext,
  useNavigationType,
  useOutlet,
  useResolvedPath,
} from "react-router-dom";

export default function Message() {
  console.log("useInRouterContext", useInRouterContext()); // true (是否在路由中)
  console.log("useNavigationType", useNavigationType()); // push (路由类型)
  console.log("useOutlet", useOutlet()); // undefined (当前组件中渲染的嵌套路由)
  const resolvedPath = useResolvedPath("/detail?id=001&title=news#React");
  console.log("useResolvedPath", resolvedPath); // {pathname: "/detail", search: "?id=001&title=news", hash: "#React", params: {…}, state: undefined, …}

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
                to="detail"
                state={{ id: m.id, title: m.title, content: m.content }}
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

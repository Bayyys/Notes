import React, { useState } from "react";

export default function News() {
  const [news] = useState([
    {
      id: 1,
      title: "news001",
      content: "news001的内容",
    },
    {
      id: 2,
      title: "news002",
      content: "news002的内容",
    },
    {
      id: 3,
      title: "news003",
      content: "news003的内容",
    },
  ]);
  return (
    <div>
      <ul>
        {news.map((newsObj) => {
          return <li key={newsObj.id}>{newsObj.title}</li>;
        })}
      </ul>
    </div>
  );
}

import React, { useState } from "react";
import { Navigate } from "react-router-dom";

export default function Home() {
  const [sum, setSum] = useState(1);
  return (
    <div>
      <h1>Home内容</h1>
      {sum === 2 ? (
        <Navigate to="/about" replace={true} />
      ) : (
        <h2>当前sum值为: {sum}</h2>
      )}
      <button
        onClick={() => {
          setSum(2);
        }}
      >
        sum=2
      </button>
    </div>
  );
}

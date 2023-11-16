import { useState } from "react";

export default function App() {
  const [count, setCount] = useState(0);
  const [select, setSelect] = useState(1);
  return (
    <div id="app">
      <p>点击了 {count} 次</p>
      <div>
        <select
          onChange={(e) => {
            setSelect(e.target.value);
          }}
        >
          {[1, 2, 3, 4, 5].map((item) => (
            <option key={item} value={item}>
              {item}
            </option>
          ))}
        </select>{" "}
        &nbsp;&nbsp;
        <button onClick={() => setCount(count + select)}>+</button>
        &nbsp;&nbsp;
        <button onClick={() => setCount(count - select)}>-</button>
        &nbsp;&nbsp;
        <button
          onClick={() => {
            if (count % 2 !== 0) {
              setCount(count + select);
            }
          }}
        >
          +(odd)
        </button>
        &nbsp;&nbsp;
        <button
          onClick={() => {
            setTimeout(() => {
              setCount(count + select);
            }, 1000);
          }}
        >
          +(async)
        </button>
      </div>
    </div>
  );
}

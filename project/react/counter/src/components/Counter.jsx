import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  increment,
  decrement,
  incrementIfOdd,
  incrementAsync,
} from "../redux/counter";

export default function Counter() {
  const count = useSelector((state) => state.counter.value);
  const tenTimes = useSelector((state) => state.counter.value * 10);
  const dispatch = useDispatch();
  const [select, setSelect] = useState(1);
  return (
    <div id="app">
      <p>点击了 {count} 次</p>
      <p>10倍后结果为 {tenTimes}</p>
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
        <button onClick={() => dispatch(increment(select))}>+</button>
        &nbsp;&nbsp;
        <button onClick={() => dispatch(decrement(select))}>-1</button>
        &nbsp;&nbsp;
        <button
          onClick={() => {
            dispatch(incrementIfOdd());
          }}
        >
          +(odd)
        </button>
        &nbsp;&nbsp;
        <button
          onClick={() => {
            dispatch(incrementAsync(select, 1000));
          }}
        >
          +(async)
        </button>
      </div>
    </div>
  );
}

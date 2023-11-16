import { useState } from "react";
import { connect } from "react-redux";
import {
  increment,
  decrement,
  incrementIfOdd,
  incrementAsync,
} from "./redux/counter";

function App(props) {
  const count = props.count;
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
        <button onClick={() => props.increment(select)}>+</button>
        &nbsp;&nbsp;
        <button onClick={() => props.decrement(select)}>-1</button>
        &nbsp;&nbsp;
        <button
          onClick={() => {
            props.incrementIfOdd();
          }}
        >
          +(odd)
        </button>
        &nbsp;&nbsp;
        <button
          onClick={() => {
            props.incrementAsync(select, 1000);
          }}
        >
          +(async)
        </button>
      </div>
    </div>
  );
}

export default connect(
  (state) => ({
    count: state.counter.value,
  }),
  {
    increment,
    decrement,
    incrementIfOdd,
    incrementAsync,
  }
)(App);

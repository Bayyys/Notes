// import React, { Component } from "react";

// export default class ReactHooks extends Component {
//   state = {
//     count: 0,
//   };

//   myRef = React.createRef();

//   componentDidMount() {
//     this.token = setInterval(() => {
//       this.setState((state) => ({ count: state.count + 1 }));
//     }, 1000);
//   }

//   componentWillUnmount() {
//     clearInterval(this.token);
//   }

//   add = () => {
//     this.setState((state) => ({ count: state.count + 1 }));
//   };

//   show = () => {
//     console.log(this.myRef.current.value);
//   };

//   render() {
//     return (
//       <div>
//         <input placeholder="请输入用户名" ref={this.myRef} />
//         <h1>当前求和为: {this.state.count}</h1>
//         <button onClick={this.add}>+1</button>
//         <button onClick={this.show}>展示用户名</button>
//       </div>
//     );
//   }
//   this;
// }

import React from "react";

export default function Count() {
  const [count, setCount] = React.useState(0);
  const myRef = React.useRef();

  React.useEffect(() => {
    const token = setInterval(() => {
      setCount((count) => count + 1);
    }, 1000);
    return () => {
      clearInterval(token);
    };
  }, []); // 数组内的内容为依赖项, 当依赖项发生变化时, 执行useEffect内的函数

  return (
    <div>
      <h1>当前求和为: {count}</h1>
      <input placeholder="请输入用户名" ref={myRef} />
      <button onClick={() => setCount(count + 1)}>+1</button>
      <button onClick={() => console.log(myRef.current.value)}>展示</button>
    </div>
  );
}

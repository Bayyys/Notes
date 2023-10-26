import React, { Component } from "react";
// import SetStateDemo from "./components/1_setState";
// import LazyLoad from "./components/2_lazyLoad";
// import { BrowserRouter } from "react-router-dom";
// import Count from "./components/3_hooks";
// import FragmentDemo from "./components/4_fragment";
// import ContextDemo from "./components/5_context";
// import Demo from "./components/6_optimize";
// import Demo from "./components/7_reander_props";
import Demo from "./components/8_error_boundary/Parent";

export default class App extends Component {
  render() {
    return (
      <div>
        <Demo />
      </div>
    );
  }
}

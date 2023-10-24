import React, { Component } from "react";
// import SetStateDemo from "./components/1_setState";
import LazyLoad from "./components/2_lazyLoad";
import { BrowserRouter } from "react-router-dom";

export default class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <LazyLoad />
      </BrowserRouter>
    );
  }
}

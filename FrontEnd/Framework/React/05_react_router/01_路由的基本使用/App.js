import React, { Component } from "react";
import Show from "./components/Show";
import { BrowserRouter } from "react-router-dom";

export default class App extends Component {
  render() {
    return (
      <div className="container">
        <BrowserRouter>
          <Show />
        </BrowserRouter>
      </div>
    );
  }
}

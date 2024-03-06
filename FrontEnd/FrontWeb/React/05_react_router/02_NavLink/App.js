import React, { Component } from "react";
import { NavLink, Route } from "react-router-dom";
import About from "./pages/About";
import Home from "./pages/Home";
import Header from "./components/Header/Header";

export default class App extends Component {
  render() {
    return (
      <div>
        <div className="row">
          <Header />
        </div>
        <div className="row">
          <div className="col-xs-2 col-xs-offset-2 list-group">
            <NavLink activeClassName='active' className="list-group-item" to="/about">
              About
            </NavLink>
            <NavLink activeClassName='active' className="list-group-item" to="/home">
              Home
            </NavLink>
          </div>
          <div className="col-xs-6 panel panel-body">
            <Route path="/about" component={About} />
            <Route path="/home" component={Home} />
          </div>
        </div>
      </div>
    );
  }
}

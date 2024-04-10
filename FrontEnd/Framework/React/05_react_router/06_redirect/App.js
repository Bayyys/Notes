import React, { Component } from "react";
import { Route, Redirect } from "react-router-dom";
import About from "./pages/About";
import Home from "./pages/Home";
import Header from "./components/Header/Header";
import MyNavLink from "./components/Header/MyNavLink";

export default class App extends Component {
  render() {
    return (
      <div>
        <div className="row">
          <Header />
        </div>
        <div className="row">
          <div className="col-xs-2 col-xs-offset-2 list-group">
            <MyNavLink to="/about">About</MyNavLink>
            <MyNavLink to="/home">Home</MyNavLink>
          </div>
          <div className="col-xs-6 panel panel-body">
            <Route path="/about" component={About} />
            <Route path="/home" component={Home} />
            <Redirect to="/about" />
          </div>
        </div>
      </div>
    );
  }
}

import React, { Component } from "react";
import { Link, Route } from "react-router-dom";
import About from "../pages/About";
import Home from "../pages/Home";

export default class Show extends Component {
  render() {
    return (
      <div>
        <div className="row">
          <div className="col-xs-offset-2 col-xs-8">
            <div className="page-header">
              <h2>React Router Demo</h2>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-xs-2 col-xs-offset-2 list-group">
            <Link className="list-group-item" to="/about">
              About
            </Link>
            <Link className="list-group-item" to="/home">
              Home
            </Link>
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

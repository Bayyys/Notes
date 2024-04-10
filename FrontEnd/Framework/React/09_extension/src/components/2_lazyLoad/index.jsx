import React, { Component, Suspense, lazy } from "react";
import { NavLink, Redirect, Route, Switch } from "react-router-dom";

const Home = lazy(() => import("./Home"));
const About = lazy(() => import("./About"));

export default class LazyLoad extends Component {
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
            <NavLink className="list-group-item" to="/about">
              About
            </NavLink>
            <NavLink className="list-group-item" to="/home">
              Home
            </NavLink>
          </div>
          <div className="col-xs-6 panel panel-body">
            <Suspense fallback={<h1>Loading...</h1>}>
              <Switch>
                <Route path="/about" component={About} />
                <Route path="/home" component={Home} />
                <Redirect to="/about" />
              </Switch>
            </Suspense>
          </div>
        </div>
      </div>
    );
  }
}

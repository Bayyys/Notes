import React from "react";
import { NavLink, useRoutes } from "react-router-dom";
import routes from "./routes";

export default function App() {
  const element = useRoutes(routes);
  return (
    <div>
      <div className="row">
        <div className="col-xs-offset-2 col-xs-8 page-header">
          <h2>React Router 6</h2>
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
        <div className="col-xs-6 panel panel-body">{element}</div>
      </div>
    </div>
  );
}

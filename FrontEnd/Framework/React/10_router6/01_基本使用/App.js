import React from "react";
import { NavLink, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";

export default function App() {
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
        <div className="col-xs-6 panel panel-body">
          {/* Routes 代替 Switch */}
          <Routes>
            {/* element 代替 component */}
            <Route path="/about" element={<About />} />
            <Route path="/home" element={<Home />} />
            {/* path='/' 代替 Redirect */}
            <Route path="/" element={<Home />} />
          </Routes>
        </div>
      </div>
    </div>
  );
}

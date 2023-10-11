import React, { Suspense, lazy } from "react";
import { Link, Routes, Route } from "react-router-dom";
import { Button } from "antd";
// import Home from "./pages/Home";
// import About from "./pages/About";

const Home = lazy(() => import(/* WebpackChunkName: "home" */ "./pages/Home"));
const About = lazy(() =>
  import(/* WebpackChunkName: "about" */ "./pages/About")
);

function App() {
  return (
    <div className="App">
      <h1>App</h1>
      <Button type="primary">Button</Button>
      <ul>
        <li>
          <Link to="/home">Home</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
      </ul>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Suspense>
    </div>
  );
}

export default App;

import { Navigate } from "react-router-dom";
import Home from "../pages/Home";
import About from "../pages/About";

const routes = [
  {
    path: "/about",
    element: <About />,
  },
  {
    path: "/home",
    element: <Home />,
  },
  {
    path: "/",
    element: <Navigate to="/about" />,
  },
];

export default routes;

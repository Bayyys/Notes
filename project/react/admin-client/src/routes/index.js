import { Navigate } from "react-router-dom";
import Login from "../pages/Login/Login";
import Register from "../pages/Register/Register";
import Admin from "../pages/Admin/Admin";

const routes = [
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/register",
    element: <Register />,
  },
  {
    path: "/admin",
    element: <Admin />,
  },
  {
    path: "/",
    element: <Navigate to="/login" />,
  },
];

export default routes;

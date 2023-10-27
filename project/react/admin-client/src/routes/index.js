import { Navigate } from "react-router-dom";
import Login from "../pages/Login";
import Register from "../pages/Register";

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
    path: "/",
    element: <Navigate to="/login" />,
  },
];

export default routes;

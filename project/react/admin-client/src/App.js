import React from "react";
import { Button, message } from "antd";
import { NavLink, useRoutes } from "react-router-dom";
import routes from "./routes";

export default function App() {
  const element = useRoutes(routes);

  const showMessage = () => {
    message.info("This is a normal message");
  };

  return (
    <div>
      <h1>APP</h1>
      <Button type="primary" onClick={showMessage}>
        Button
      </Button>
      <NavLink to="/login">Login</NavLink>
      <NavLink to="/register">Register</NavLink>
      {element}
    </div>
  );
}

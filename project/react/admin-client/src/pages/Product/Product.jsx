import React from "react";
import { Outlet } from "react-router-dom";
import { useNavigate } from "react-router-dom";

export default function Product() {
  const navigate = useNavigate();

  return (
    <>
      <Outlet />
    </>
  );
}

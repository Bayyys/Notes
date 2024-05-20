"use client";
import React, { use, useEffect, useState } from "react";
import { SignOut } from "@/app/components/auth/signout-button";

const Page = () => {
  const [data, setData] = useState({});
  useEffect(() => {
    fetch("/api/user")
      .then((res) => res.json())
      .then(
        (res) => {
          console.log(res);
          setData(res);
        },
        (error) => {
          console.log(error);
        }
      );
  }, [setData]);
  return (
    <>
      <SignOut />
    </>
  );
};
export default Page;

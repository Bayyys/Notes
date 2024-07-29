"use client";
import axios from "axios";
import "@/mock/index";

export default function Home() {
  const handlerClick = async () => {
    const res = await axios.get("/user/list");
    console.log("🚀 ~ handlerClick ~ res:", res.data.data);
  };

  return (
    <>
      <h1>Hello World</h1>
      <button onClick={handlerClick}>Click me</button>
    </>
  );
}

// useEffectEvent 在 React 稳定版中 还没有发布
import { useEffect, useState } from "react";

export default function UseEffectEventDemo() {
  const [fName, setFName] = useState("");
  const [lName, setLName] = useState("");

  useEffect(() => {
    setFName("John");
    setLName("Doe");
  }, [fName, lName]);

  return (
    <>
      <h2>UseEffect Event Demo</h2>
      <p>First Name: {fName}</p>
      <p>Last Name: {lName}</p>
    </>
  );
}
